"""Simple data quality helpers for learning projects.

These helpers flag possible issues for review. They do not decide whether data
should be removed.
"""

import pandas as pd
import numpy as np


def _require_columns(df: pd.DataFrame, columns) -> None:
    """Raise a clear error if expected columns are missing."""
    missing = [col for col in columns if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")


def missing_value_report(df: pd.DataFrame) -> pd.DataFrame:
    """Return missing value counts and percentages by column."""
    report = pd.DataFrame({
        "column": df.columns,
        "missing_count": df.isna().sum().values,
        "missing_percent": (df.isna().mean().values * 100).round(2),
    })
    return report


def flag_outliers_zscore(df: pd.DataFrame, group_cols, value_col: str, threshold: float = 1.5) -> pd.DataFrame:
    """Flag potential outliers using within-group z-scores.

    The `qc_flag` column is a review prompt. It is not a removal decision.
    """
    if isinstance(group_cols, str):
        group_cols = [group_cols]
    _require_columns(df, [*group_cols, value_col])
    if threshold <= 0:
        raise ValueError("threshold must be positive.")
    result = df.copy()
    result["group_mean"] = result.groupby(group_cols)[value_col].transform("mean")
    result["group_sd"] = result.groupby(group_cols)[value_col].transform("std")
    result["z_score"] = (result[value_col] - result["group_mean"]) / result["group_sd"]
    result["qc_flag"] = np.where(result["z_score"].abs() > threshold, "review", "ok")
    result.loc[result["group_sd"].fillna(0) == 0, "qc_flag"] = "ok"
    return result


def simple_data_quality_score(df: pd.DataFrame, required_cols: list[str], min_rows: int = 6) -> dict:
    """Create a simple educational data quality score."""
    if min_rows < 1:
        raise ValueError("min_rows must be at least 1.")
    score = 0
    notes = []

    missing_cols = [c for c in required_cols if c not in df.columns]
    if not missing_cols:
        score += 30
    else:
        notes.append(f"Missing columns: {missing_cols}")

    if df.isna().sum().sum() == 0:
        score += 25
    else:
        notes.append("Missing values detected.")

    if len(df) >= min_rows:
        score += 20
    else:
        notes.append("Dataset is very small.")

    numeric_cols = df.select_dtypes(include="number").columns
    if len(numeric_cols) > 0:
        score += 10
    else:
        notes.append("No numeric columns detected.")

    score += 15  # basic structure present

    return {"score": min(score, 100), "notes": notes}
