import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from src.enzyme_kinetics import fit_michaelis_menten, make_prediction_table, summarize_velocity

# Synthetic enzyme kinetics dataset for learning only.
df = pd.read_csv("data/enzyme_kinetics/michaelis_menten_clean.csv")

summary = summarize_velocity(df)
params = fit_michaelis_menten(summary)
curve = make_prediction_table(
    params,
    min_substrate=summary["substrate_mM"].min(),
    max_substrate=summary["substrate_mM"].max(),
)

fig = px.scatter(
    summary,
    x="substrate_mM",
    y="mean_velocity",
    error_y="sem_velocity",
    title="Synthetic Michaelis-Menten-style Curve",
    labels={"substrate_mM": "Substrate (mM)", "mean_velocity": "Mean Initial Velocity"},
)
fig.add_trace(
    go.Scatter(
        x=curve["substrate_mM"],
        y=curve["predicted_velocity"],
        mode="lines",
        name="Fitted curve",
    )
)
fig.show()

print({"educational_vmax": round(params["vmax"], 3), "educational_km": round(params["km"], 3)})
