"""Reusable Plotly plotting helpers for synthetic teaching datasets."""

import pandas as pd
import numpy as np
import plotly.express as px


def _require_columns(df: pd.DataFrame, columns) -> None:
    """Raise a clear error if expected columns are missing."""
    missing = [col for col in columns if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")


def plot_group_means(summary_df: pd.DataFrame, group_col: str, mean_col: str, sem_col: str, title: str):
    """Create a bar chart with SEM error bars."""
    _require_columns(summary_df, [group_col, mean_col, sem_col])
    return px.bar(summary_df, x=group_col, y=mean_col, error_y=sem_col, title=title)


def plot_dose_response(summary_df: pd.DataFrame):
    """Create an interactive dose-response curve."""
    _require_columns(
        summary_df,
        ["drug_name", "concentration_uM", "mean_viability", "sem_viability", "sd_viability", "n"],
    )
    plot_df = summary_df.copy()
    plot_df["plot_concentration"] = plot_df["concentration_uM"].replace(0, 0.001)
    fig = px.line(
        plot_df,
        x="plot_concentration",
        y="mean_viability",
        color="drug_name",
        markers=True,
        error_y="sem_viability",
        hover_data=["concentration_uM", "sd_viability", "n"],
        title="Dose-Response Visualization",
    )
    fig.update_xaxes(type="log", title="Concentration (uM, log scale; 0 plotted as 0.001)")
    fig.update_yaxes(title="Mean Cell Viability (%)")
    return fig


def plot_fold_change(summary_df: pd.DataFrame):
    """Create a fold-change bar chart."""
    _require_columns(summary_df, ["gene", "log2_fold_change"])
    return px.bar(
        summary_df.sort_values("log2_fold_change"),
        x="gene",
        y="log2_fold_change",
        title="Toy Gene Expression: log2 Fold Change",
    )


def plot_heatmap(expr_df: pd.DataFrame):
    """Create a gene-wise z-score heatmap from a gene x sample expression matrix."""
    if expr_df.empty:
        raise ValueError("expr_df must contain at least one gene and one sample.")
    expr_z = expr_df.sub(expr_df.mean(axis=1), axis=0).div(expr_df.std(axis=1), axis=0)
    return px.imshow(expr_z, aspect="auto", title="Gene Expression Heatmap")


def make_pca_sample_scores(expr_df: pd.DataFrame) -> pd.DataFrame:
    """Create simple PCA-style sample scores from a gene x sample matrix.

    This uses NumPy SVD so students do not need an additional PCA package.
    """
    if expr_df.empty or expr_df.shape[1] < 2:
        raise ValueError("expr_df must include genes as rows and at least two sample columns.")
    sample_by_gene = expr_df.T
    scaled = (sample_by_gene - sample_by_gene.mean(axis=0)) / sample_by_gene.std(axis=0)
    scaled = scaled.replace([np.inf, -np.inf], np.nan).fillna(0)
    u, s, _ = np.linalg.svd(scaled, full_matrices=False)
    return pd.DataFrame({
        "sample": sample_by_gene.index,
        "PC1": u[:, 0] * s[0],
        "PC2": u[:, 1] * s[1] if len(s) > 1 else 0,
    })


def plot_pca_sample_map(pca_df: pd.DataFrame):
    """Create a PCA-style sample map from `make_pca_sample_scores()` output."""
    _require_columns(pca_df, ["sample", "PC1", "PC2"])
    plot_df = pca_df.copy()
    if "group" not in plot_df.columns:
        plot_df["group"] = plot_df["sample"].str.extract(r"(control|treat_low|treat_high|treatment)")
    return px.scatter(
        plot_df,
        x="PC1",
        y="PC2",
        color="group",
        text="sample",
        title="Toy PCA-style Sample Map",
    )
