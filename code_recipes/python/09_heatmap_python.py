import plotly.express as px

def plot_gene_expression_heatmap(expr_df):
    # expr_df should have genes as index and samples as columns
    expr_z = expr_df.sub(expr_df.mean(axis=1), axis=0).div(expr_df.std(axis=1), axis=0)
    fig = px.imshow(expr_z, aspect="auto", title="Gene Expression Heatmap")
    return fig
