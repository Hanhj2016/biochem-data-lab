import plotly.express as px

def plot_group_means(summary_df, group_col, mean_col, sem_col, title):
    fig = px.bar(summary_df, x=group_col, y=mean_col, error_y=sem_col, title=title)
    return fig
