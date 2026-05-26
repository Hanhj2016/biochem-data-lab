"""Helpers for synthetic 96-well plate QC examples."""

import pandas as pd


def _require_columns(df: pd.DataFrame, columns) -> None:
    missing = [col for col in columns if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")


def add_plate_position_flags(df: pd.DataFrame, row_col: str = "row", column_col: str = "column") -> pd.DataFrame:
    """Add simple edge-well flags for 96-well-style plate data."""
    _require_columns(df, [row_col, column_col])
    result = df.copy()
    result["is_edge_well"] = result[row_col].isin(["A", "H"]) | result[column_col].isin([1, 12])
    return result


def summarize_edge_effect(
    df: pd.DataFrame,
    value_col: str = "cell_viability_percent",
    sample_type_col: str = "sample_type",
) -> pd.DataFrame:
    """Compare mean values for edge and non-edge wells by sample type."""
    _require_columns(df, ["is_edge_well", value_col, sample_type_col])
    return (
        df.groupby([sample_type_col, "is_edge_well"])
        .agg(mean_value=(value_col, "mean"), sd_value=(value_col, "std"), n=(value_col, "count"))
        .reset_index()
    )


def make_plate_matrix(
    df: pd.DataFrame,
    value_col: str = "cell_viability_percent",
    row_col: str = "row",
    column_col: str = "column",
) -> pd.DataFrame:
    """Create a row x column matrix for heatmap plotting."""
    _require_columns(df, [row_col, column_col, value_col])
    matrix = df.pivot(index=row_col, columns=column_col, values=value_col)
    return matrix.sort_index()
