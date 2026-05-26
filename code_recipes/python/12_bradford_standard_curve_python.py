import pandas as pd
import plotly.express as px

from src.standard_curve import (
    estimate_unknown_concentrations,
    fit_linear_standard_curve,
    summarize_standard_curve,
    summarize_unknown_estimates,
)

# Synthetic Bradford-style standard curve dataset for learning only.
df = pd.read_csv("data/standard_curves/bradford_standard_curve.csv")

standard_summary = summarize_standard_curve(df)
fit = fit_linear_standard_curve(df)
unknown_estimates = estimate_unknown_concentrations(df, fit)
unknown_summary = summarize_unknown_estimates(unknown_estimates)

fig = px.scatter(
    standard_summary,
    x="known_concentration_mg_ml",
    y="mean_absorbance",
    error_y="sem_absorbance",
    title="Synthetic Bradford-style Standard Curve",
    labels={
        "known_concentration_mg_ml": "Known concentration (mg/mL)",
        "mean_absorbance": "Mean absorbance at 595 nm",
    },
)
fig.add_scatter(
    x=standard_summary["known_concentration_mg_ml"],
    y=fit["slope"] * standard_summary["known_concentration_mg_ml"] + fit["intercept"],
    mode="lines",
    name="Linear fit",
)
fig.show()

print({"slope": round(fit["slope"], 3), "intercept": round(fit["intercept"], 3), "r_squared": round(fit["r_squared"], 4)})
print(unknown_summary)
