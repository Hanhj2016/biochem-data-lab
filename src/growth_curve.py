"""Helpers for synthetic OD600 growth curve examples."""

import numpy as np
import pandas as pd


def _require_columns(df: pd.DataFrame, columns) -> None:
    missing = [col for col in columns if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")


def summarize_growth(df: pd.DataFrame) -> pd.DataFrame:
    """Summarize OD600 by strain and time."""
    _require_columns(df, ["strain", "time_hr", "od600"])
    summary = (
        df.groupby(["strain", "time_hr"])
        .agg(mean_od600=("od600", "mean"), sd_od600=("od600", "std"), n=("od600", "count"))
        .reset_index()
    )
    summary["sem_od600"] = summary["sd_od600"] / np.sqrt(summary["n"])
    return summary


def estimate_log_phase_rate(summary_df: pd.DataFrame, start_hr: float = 2, end_hr: float = 6) -> pd.DataFrame:
    """Estimate a simple log-phase rate from ln(OD600) over a chosen time window."""
    _require_columns(summary_df, ["strain", "time_hr", "mean_od600"])
    rows = []
    for strain, group in summary_df.groupby("strain"):
        window = group[(group["time_hr"] >= start_hr) & (group["time_hr"] <= end_hr)]
        if len(window) < 2:
            continue
        slope, intercept = np.polyfit(window["time_hr"], np.log(window["mean_od600"]), 1)
        rows.append({"strain": strain, "log_phase_rate_per_hr": slope, "doubling_time_hr": np.log(2) / slope})
    return pd.DataFrame(rows)
