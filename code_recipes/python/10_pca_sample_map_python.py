import pandas as pd
import numpy as np
import plotly.express as px

# Load a synthetic gene expression matrix.
# Rows are genes; columns are samples.
df = pd.read_csv("data/gene_expression/gene_expression_matrix_pca.csv")

expr = df.set_index("gene")

# PCA-style sample map using NumPy SVD.
# Samples should be rows and genes should be columns.
sample_by_gene = expr.T
sample_by_gene_scaled = (sample_by_gene - sample_by_gene.mean(axis=0)) / sample_by_gene.std(axis=0)

u, s, vt = np.linalg.svd(sample_by_gene_scaled, full_matrices=False)

pca_df = pd.DataFrame({
    "sample": sample_by_gene_scaled.index,
    "PC1": u[:, 0] * s[0],
    "PC2": u[:, 1] * s[1],
})
pca_df["group"] = pca_df["sample"].str.extract(r"(control|treat_low|treat_high)")

fig = px.scatter(
    pca_df,
    x="PC1",
    y="PC2",
    color="group",
    text="sample",
    title="Toy PCA-style Sample Map",
)
fig.show()
