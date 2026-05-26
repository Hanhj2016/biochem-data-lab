"""Helpers for synthetic standard curve / assay calibration examples.

Example:
    df = pd.read_csv("data/standard_curves/bradford_standard_curve.csv")
    fit = fit_linear_standard_curve(df)
    estimates = estimate_unknown_concentrations(df, fit)
"""

import numpy as np
import pandas as pd
from scipy import stats


def _require_columns(df: pd.DataFrame, columns) -> None:
    """Raise a clear error if expected columns are missing."""
    missing = [col for col in columns if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")


def summarize_standard_curve(
    df: pd.DataFrame,
    concentration_col: str = "known_concentration_mg_ml",
    absorbance_col: str = "absorbance_595",
    sample_type_col: str = "sample_type",
) -> pd.DataFrame:
    """Summarize standard absorbance by known concentration."""
    _require_columns(df, [concentration_col, absorbance_col, sample_type_col])
    standards = df[df[sample_type_col] == "standard"].dropna(subset=[concentration_col])
    if standards.empty:
        raise ValueError("No standard rows found.")
    summary = (
        standards.groupby(concentration_col)
        .agg(
            mean_absorbance=(absorbance_col, "mean"),
            sd_absorbance=(absorbance_col, "std"),
            n=(absorbance_col, "count"),
        )
        .reset_index()
    )
    summary["sem_absorbance"] = summary["sd_absorbance"] / np.sqrt(summary["n"])
    return summary


def fit_linear_standard_curve(
    df: pd.DataFrame,
    concentration_col: str = "known_concentration_mg_ml",
    absorbance_col: str = "absorbance_595",
    sample_type_col: str = "sample_type",
) -> dict:
    """Fit absorbance = slope * concentration + intercept using standard rows."""
    _require_columns(df, [concentration_col, absorbance_col, sample_type_col])
    standards = df[df[sample_type_col] == "standard"].dropna(subset=[concentration_col, absorbance_col])
    if standards[concentration_col].nunique() < 2:
        raise ValueError("At least two standard concentrations are needed.")
    result = stats.linregress(standards[concentration_col], standards[absorbance_col])
    return {
        "slope": float(result.slope),
        "intercept": float(result.intercept),
        "r_squared": float(result.rvalue ** 2),
        "min_standard": float(standards[concentration_col].min()),
        "max_standard": float(standards[concentration_col].max()),
    }


def estimate_unknown_concentrations(
    df: pd.DataFrame,
    fit: dict,
    sample_id_col: str = "sample_id",
    sample_type_col: str = "sample_type",
    absorbance_col: str = "absorbance_595",
) -> pd.DataFrame:
    """Estimate unknown concentrations from a fitted linear standard curve."""
    _require_columns(df, [sample_id_col, sample_type_col, absorbance_col])
    if fit["slope"] == 0:
        raise ValueError("Cannot estimate concentrations with a zero slope.")
    unknowns = df[df[sample_type_col] == "unknown"].copy()
    if unknowns.empty:
        raise ValueError("No unknown rows found.")
    unknowns["estimated_concentration_mg_ml"] = (unknowns[absorbance_col] - fit["intercept"]) / fit["slope"]
    unknowns["outside_standard_range"] = (
        (unknowns["estimated_concentration_mg_ml"] < fit["min_standard"])
        | (unknowns["estimated_concentration_mg_ml"] > fit["max_standard"])
    )
    return unknowns


def summarize_unknown_estimates(
    estimates: pd.DataFrame,
    sample_id_col: str = "sample_id",
    estimate_col: str = "estimated_concentration_mg_ml",
) -> pd.DataFrame:
    """Summarize replicate concentration estimates by unknown sample prefix."""
    _require_columns(estimates, [sample_id_col, estimate_col, "outside_standard_range"])
    result = estimates.copy()
    result["unknown_id"] = result[sample_id_col].str.extract(r"(UNK_[A-Za-z0-9]+)")
    summary = (
        result.groupby("unknown_id")
        .agg(
            mean_estimated_concentration=(estimate_col, "mean"),
            sd_estimated_concentration=(estimate_col, "std"),
            n=(estimate_col, "count"),
            any_outside_standard_range=("outside_standard_range", "any"),
        )
        .reset_index()
    )
    summary["sem_estimated_concentration"] = summary["sd_estimated_concentration"] / np.sqrt(summary["n"])
    return summary
