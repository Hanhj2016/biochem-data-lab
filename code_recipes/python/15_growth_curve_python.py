import pandas as pd
import plotly.express as px

from src.growth_curve import estimate_log_phase_rate, summarize_growth

df = pd.read_csv("data/growth_curve/bacterial_growth_curve.csv")
summary = summarize_growth(df)
rates = estimate_log_phase_rate(summary)

fig = px.line(
    summary,
    x="time_hr",
    y="mean_od600",
    color="strain",
    markers=True,
    error_y="sem_od600",
    title="Synthetic OD600 Growth Curve",
)
fig.show()

print(rates)
