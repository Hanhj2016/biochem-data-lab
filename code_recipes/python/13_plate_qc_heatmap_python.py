import pandas as pd
import plotly.express as px

from src.plate_qc import add_plate_position_flags, make_plate_matrix, summarize_edge_effect

df = pd.read_csv("data/assay_qc/plate_layout_edge_effect.csv")
df_qc = add_plate_position_flags(df)
edge_summary = summarize_edge_effect(df_qc)
plate_matrix = make_plate_matrix(df_qc)

fig = px.imshow(
    plate_matrix,
    aspect="auto",
    title="Synthetic 96-well Plate QC Heatmap",
    labels={"x": "Column", "y": "Row", "color": "Cell viability (%)"},
)
fig.show()

print(edge_summary)
