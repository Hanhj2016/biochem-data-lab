"""Reusable beginner-friendly statistics helpers for Biochemistry datasets."""

import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols


def summary_mean_sd_sem(df: pd.DataFrame, group_cols, value_col: str) -> pd.DataFrame:
    """Calculate mean, SD, n, and SEM by group."""
    if isinstance(group_cols, str):
        group_cols = [group_cols]
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
    a = df[df[group_col] == group_a][value_col].dropna()
    b = df[df[group_col] == group_b][value_col].dropna()
    return stats.ttest_ind(a, b, equal_var=False)


def run_anova(df: pd.DataFrame, group_col: str, value_col: str) -> pd.DataFrame:
    """Run one-way ANOVA using statsmodels."""
    model = ols(f"{value_col} ~ C({group_col})", data=df).fit()
    return sm.stats.anova_lm(model, typ=2)


def calculate_fold_change(df: pd.DataFrame, control_cols: list[str], treatment_cols: list[str]) -> pd.DataFrame:
    """Calculate mean control, mean treatment, fold change, and log2 fold change."""
    result = df.copy()
    result["control_mean"] = result[control_cols].mean(axis=1)
    result["treatment_mean"] = result[treatment_cols].mean(axis=1)
    result["fold_change"] = result["treatment_mean"] / result["control_mean"]
    result["log2_fold_change"] = np.log2(result["fold_change"])
    return result
