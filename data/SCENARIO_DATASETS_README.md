# Scenario Datasets

All datasets in this folder are synthetic and for learning only. They are not real experimental, patient, clinical, proprietary, diagnostic, regulatory, or drug-efficacy data.

The goal is to give students small Biochemistry-first examples for practicing data loading, summary statistics, visualization, quality checks, and cautious interpretation.

## Enzyme Activity

| Dataset | What it teaches |
|---|---|
| `data/enzyme_activity/enzyme_activity_clean.csv` | Clean two-group enzyme activity comparison with clear separation between control and treatment. |
| `data/enzyme_activity/enzyme_activity_noisy.csv` | Same basic comparison with more replicate variability, useful for discussing SD, SEM, and cautious wording. |
| `data/enzyme_activity/enzyme_activity_outlier.csv` | One treatment replicate is unusually high, useful for QC review and outlier discussion. |
| `data/enzyme_activity/enzyme_activity_missing_values.csv` | Blank activity values, useful for missing-value reports and explaining `dropna()` or `na.rm = TRUE`. |
| `data/enzyme_activity/enzyme_activity_three_groups.csv` | Control, low inhibitor, and high inhibitor groups for ANOVA-style practice. |

## Drug Response

| Dataset | What it teaches |
|---|---|
| `data/drug_response/drug_response_clear.csv` | Clear synthetic concentration-response pattern for two compounds. |
| `data/drug_response/drug_response_weak.csv` | Weak response pattern where overinterpretation should be avoided. |
| `data/drug_response/drug_response_noisy.csv` | Noisier replicate values for discussing variability and visual confidence. |
| `data/drug_response/drug_response_missing_replicate.csv` | Uneven replicate counts across concentrations, useful for checking `n`. |
| `data/drug_response/drug_response_outlier.csv` | Suspicious replicate values that should be flagged for review, not automatically removed. |
| `data/drug_response/drug_response_three_compounds.csv` | Three-compound comparison for plotting, grouping, and legend-reading practice. |
| `data/drug_response/drug_response_ic50_like.csv` | Smooth synthetic IC50-style curve-fitting practice with four replicates per concentration. |

## Gene Expression

| Dataset | What it teaches |
|---|---|
| `data/gene_expression/gene_expression_small_clean.csv` | Small clean fold-change example with target and stable genes. |
| `data/gene_expression/gene_expression_with_housekeeping.csv` | Adds a `gene_type` column so students can compare target-related and housekeeping genes. |
| `data/gene_expression/gene_expression_treatment_gradient.csv` | Low, medium, and high treatment pattern for visualizing dose-like expression trends. |
| `data/gene_expression/gene_expression_noisy.csv` | Noisy treatment replicates for discussing variability and why fold change alone is limited. |
| `data/gene_expression/gene_expression_matrix_pca.csv` | Gene-by-sample matrix for heatmap and PCA-style visualization practice. |

## Enzyme Kinetics

| Dataset | What it teaches |
|---|---|
| `data/enzyme_kinetics/michaelis_menten_clean.csv` | Clean substrate concentration versus initial velocity pattern for Michaelis-Menten-style visualization and fitting. |
| `data/enzyme_kinetics/michaelis_menten_noisy.csv` | Same pattern with more replicate variability, useful for discussing confidence and model limitations. |

Columns include `sample_id`, `substrate_mM`, `replicate`, and `initial_velocity`.

## Standard Curves

| Dataset | What it teaches |
|---|---|
| `data/standard_curves/bradford_standard_curve.csv` | Bradford-style standard curve practice with known protein standards and unknown samples. |

Teaching focus: calibration curves, linear range, unknown concentration estimates, and why extrapolation is risky.

## Assay QC / Plate Layout

| Dataset | What it teaches |
|---|---|
| `data/assay_qc/plate_layout_edge_effect.csv` | 96-well-style layout with controls, treatment wells, and a mild synthetic edge-effect pattern for QC heatmap practice. |

## qPCR

| Dataset | What it teaches |
|---|---|
| `data/qpcr/qpcr_delta_ct_sample.csv` | Ct values for a housekeeping gene and three target genes across control and treatment conditions. |

Teaching focus: Ct values, housekeeping normalization, delta Ct, delta-delta Ct, and relative expression.

## Growth Curves

| Dataset | What it teaches |
|---|---|
| `data/growth_curve/bacterial_growth_curve.csv` | Two synthetic strains measured over time with replicate OD600 values. |

## Synthetic Sequences

| Dataset | What it teaches |
|---|---|
| `data/sequences/synthetic_sequences.csv` | Short synthetic DNA fragments for GC content, reverse complement, motif search, and sequence-summary practice. |

## Fictional Literature Abstracts

These text files are fictional and intended for reading, summarizing, and cautious scientific writing practice:

```text
data/literature_abstracts/abstract_egfr_fictional.txt
data/literature_abstracts/abstract_enzyme_inhibitor_fictional.txt
data/literature_abstracts/abstract_biomarker_fictional.txt
data/literature_abstracts/abstract_cell_viability_fictional.txt
```

## Interpretation Boundary

Use wording such as:

```text
The synthetic data suggest...
The pattern is consistent with...
This would need validation in a real experiment...
```

Avoid wording such as:

```text
This proves...
This drug is effective...
This biomarker diagnoses...
```
