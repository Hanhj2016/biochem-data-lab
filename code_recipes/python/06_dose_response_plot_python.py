import plotly.express as px

def plot_dose_response(summary_df):
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
        title="Dose-Response Visualization"
    )
    fig.update_xaxes(type="log", title="Concentration (uM, log scale; 0 plotted as 0.001)")
    fig.update_yaxes(title="Mean Cell Viability (%)")
    return fig
