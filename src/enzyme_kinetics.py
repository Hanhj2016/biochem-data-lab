"""Beginner-friendly helpers for synthetic enzyme kinetics datasets.

Example:
    df = pd.read_csv("data/enzyme_kinetics/michaelis_menten_clean.csv")
    summary = summarize_velocity(df)
    params = fit_michaelis_menten(summary)
"""

import numpy as np
import pandas as pd
from scipy.optimize import curve_fit


def _require_columns(df: pd.DataFrame, columns) -> None:
    """Raise a clear error if expected columns are missing."""
    missing = [col for col in columns if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")


def michaelis_menten(substrate, vmax, km):
    """Return velocity from the Michaelis-Menten equation."""
    substrate = np.asarray(substrate, dtype=float)
    return (vmax * substrate) / (km + substrate)


def summarize_velocity(
    df: pd.DataFrame,
    substrate_col: str = "substrate_mM",
    velocity_col: str = "initial_velocity",
) -> pd.DataFrame:
    """Calculate mean, SD, n, and SEM by substrate concentration."""
    _require_columns(df, [substrate_col, velocity_col])
    summary = (
        df.groupby(substrate_col)
        .agg(
            mean_velocity=(velocity_col, "mean"),
            sd_velocity=(velocity_col, "std"),
            n=(velocity_col, "count"),
        )
        .reset_index()
    )
    summary["sem_velocity"] = summary["sd_velocity"] / np.sqrt(summary["n"])
    return summary


def fit_michaelis_menten(
    summary_df: pd.DataFrame,
    substrate_col: str = "substrate_mM",
    velocity_col: str = "mean_velocity",
) -> dict:
    """Fit an educational Michaelis-Menten curve to summarized data."""
    _require_columns(summary_df, [substrate_col, velocity_col])
    x = summary_df[substrate_col].astype(float)
    y = summary_df[velocity_col].astype(float)
    if len(summary_df) < 3:
        raise ValueError("At least three substrate concentrations are needed for curve fitting.")
    if (x <= 0).any():
        raise ValueError("Substrate concentrations must be positive for this simple fit.")

    start = [float(y.max()), float(x.median())]
    params, covariance = curve_fit(michaelis_menten, x, y, p0=start, bounds=(0, np.inf))
    return {
        "vmax": float(params[0]),
        "km": float(params[1]),
        "covariance": covariance,
    }


def make_prediction_table(params: dict, min_substrate: float, max_substrate: float, points: int = 100) -> pd.DataFrame:
    """Create a smooth prediction table for plotting the fitted curve."""
    if min_substrate <= 0 or max_substrate <= 0:
        raise ValueError("Substrate range must be positive.")
    if min_substrate >= max_substrate:
        raise ValueError("min_substrate must be smaller than max_substrate.")
    substrate_values = np.linspace(min_substrate, max_substrate, points)
    return pd.DataFrame({
        "substrate_mM": substrate_values,
        "predicted_velocity": michaelis_menten(substrate_values, params["vmax"], params["km"]),
    })
