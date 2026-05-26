"""Helpers for synthetic qPCR delta-delta Ct examples."""

import numpy as np
import pandas as pd


def _require_columns(df: pd.DataFrame, columns) -> None:
    missing = [col for col in columns if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")


def mean_ct_by_group(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate mean Ct by condition and gene."""
    _require_columns(df, ["condition", "gene", "ct_value"])
    return (
        df.groupby(["condition", "gene"])
        .agg(mean_ct=("ct_value", "mean"), sd_ct=("ct_value", "std"), n=("ct_value", "count"))
        .reset_index()
    )


def calculate_delta_delta_ct(df: pd.DataFrame, housekeeping_gene: str = "GAPDH", control_condition: str = "control") -> pd.DataFrame:
    """Calculate delta Ct, delta-delta Ct, and relative expression."""
    summary = mean_ct_by_group(df)
    hk = summary[summary["gene"] == housekeeping_gene][["condition", "mean_ct"]].rename(columns={"mean_ct": "housekeeping_ct"})
    merged = summary.merge(hk, on="condition", how="left")
    merged["delta_ct"] = merged["mean_ct"] - merged["housekeeping_ct"]
    control_delta = merged[merged["condition"] == control_condition][["gene", "delta_ct"]].rename(columns={"delta_ct": "control_delta_ct"})
    result = merged.merge(control_delta, on="gene", how="left")
    result["delta_delta_ct"] = result["delta_ct"] - result["control_delta_ct"]
    result["relative_expression"] = 2 ** (-result["delta_delta_ct"])
    return result[result["gene"] != housekeeping_gene].reset_index(drop=True)
