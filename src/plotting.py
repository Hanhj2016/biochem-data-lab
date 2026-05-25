"""Reusable Plotly plotting helpers."""

import pandas as pd
import plotly.express as px


def plot_group_means(summary_df: pd.DataFrame, group_col: str, mean_col: str, sem_col: str, title: str):
    """Create a bar chart with SEM error bars."""
    return px.bar(summary_df, x=group_col, y=mean_col, error_y=sem_col, title=title)


def plot_dose_response(summary_df: pd.DataFrame):
    """Create an interactive dose-response curve."""
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
    return px.bar(
        summary_df.sort_values("log2_fold_change"),
        x="gene",
        y="log2_fold_change",
        title="Toy Gene Expression: log2 Fold Change",
    )


def plot_heatmap(expr_df: pd.DataFrame):
    """Create a gene-wise z-score heatmap from a gene x sample expression matrix."""
    expr_z = expr_df.sub(expr_df.mean(axis=1), axis=0).div(expr_df.std(axis=1), axis=0)
    return px.imshow(expr_z, aspect="auto", title="Gene Expression Heatmap")
