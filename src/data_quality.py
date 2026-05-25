"""Simple data quality helpers for learning projects."""

import pandas as pd
import numpy as np


def missing_value_report(df: pd.DataFrame) -> pd.DataFrame:
    """Return missing value counts and percentages by column."""
    report = pd.DataFrame({
        "column": df.columns,
        "missing_count": df.isna().sum().values,
        "missing_percent": (df.isna().mean().values * 100).round(2),
    })
    return report


def flag_outliers_zscore(df: pd.DataFrame, group_cols, value_col: str, threshold: float = 1.5) -> pd.DataFrame:
    """Flag potential outliers using within-group z-scores."""
    if isinstance(group_cols, str):
        group_cols = [group_cols]
    result = df.copy()
    result["group_mean"] = result.groupby(group_cols)[value_col].transform("mean")
    result["group_sd"] = result.groupby(group_cols)[value_col].transform("std")
    result["z_score"] = (result[value_col] - result["group_mean"]) / result["group_sd"]
    result["qc_flag"] = np.where(result["z_score"].abs() > threshold, "review", "ok")
    return result


def simple_data_quality_score(df: pd.DataFrame, required_cols: list[str], min_rows: int = 6) -> dict:
    """Create a simple educational data quality score."""
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
