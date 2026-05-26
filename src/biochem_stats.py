"""Reusable beginner-friendly statistics helpers for Biochemistry datasets.

Example:
    df = pd.read_csv("data/enzyme_activity/enzyme_activity_clean.csv")
    summary = summary_mean_sd_sem(df, "group", "enzyme_activity")
"""

import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols


def _require_columns(df: pd.DataFrame, columns) -> None:
    """Raise a clear error if expected columns are missing."""
    missing = [col for col in columns if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")


def summary_mean_sd_sem(df: pd.DataFrame, group_cols, value_col: str) -> pd.DataFrame:
    """Calculate mean, SD, n, and SEM by group.

    Use this for grouped lab measurements such as enzyme activity by group.
    Missing values in the value column are ignored by the summary statistics.
    """
    if isinstance(group_cols, str):
        group_cols = [group_cols]
    _require_columns(df, [*group_cols, value_col])
    summary = (
        df.groupby(group_cols)
          .agg(mean_value=(value_col, "mean"),
               sd_value=(value_col, "std"),
               n=(value_col, "count"))
          .reset_index()
    )
    summary["sem_value"] = summary["sd_value"] / np.sqrt(summary["n"])
    return summary


def run_t_test(df: pd.DataFrame, group_col: str, value_col: str, group_a: str, group_b: str):
    """Run Welch's t-test between two groups."""
    _require_columns(df, [group_col, value_col])
    a = df[df[group_col] == group_a][value_col].dropna()
    b = df[df[group_col] == group_b][value_col].dropna()
    if len(a) < 2 or len(b) < 2:
        raise ValueError("Each group needs at least two non-missing values for a t-test.")
    return stats.ttest_ind(a, b, equal_var=False)


def run_anova(df: pd.DataFrame, group_col: str, value_col: str) -> pd.DataFrame:
    """Run one-way ANOVA using statsmodels."""
    _require_columns(df, [group_col, value_col])
    if df[group_col].dropna().nunique() < 2:
        raise ValueError("ANOVA needs at least two groups.")
    model = ols(f"{value_col} ~ C({group_col})", data=df).fit()
    return sm.stats.anova_lm(model, typ=2)


def calculate_fold_change(df: pd.DataFrame, control_cols: list[str], treatment_cols: list[str]) -> pd.DataFrame:
    """Calculate mean control, mean treatment, fold change, and log2 fold change."""
    _require_columns(df, [*control_cols, *treatment_cols])
    result = df.copy()
    result["control_mean"] = result[control_cols].mean(axis=1)
    result["treatment_mean"] = result[treatment_cols].mean(axis=1)
    result["fold_change"] = result["treatment_mean"] / result["control_mean"]
    result["log2_fold_change"] = np.log2(result["fold_change"])
    return result
