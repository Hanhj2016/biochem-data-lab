import pandas as pd
import plotly.express as px

from src.qpcr import calculate_delta_delta_ct

df = pd.read_csv("data/qpcr/qpcr_delta_ct_sample.csv")
results = calculate_delta_delta_ct(df)

plot_df = results[results["condition"] == "treatment"]
fig = px.bar(
    plot_df,
    x="gene",
    y="relative_expression",
    title="Synthetic qPCR Relative Expression",
    labels={"relative_expression": "Relative expression (2^-ddCt)"},
)
fig.show()

print(results)
