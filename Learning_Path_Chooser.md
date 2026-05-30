# BioChem Data Lab: Learning Path Chooser

**A Python + R + Jupyter starter kit for Biochemistry and life science data analysis**

## Purpose

Students do not need to finish every notebook. Pick one path and continue based on interest. Notebooks 14-22 are Python-first applied or advancement extensions; they revisit earlier ideas only where needed to teach a new lab-data context.


## Notebook Map By Purpose

Use this map when the numbering feels confusing. The notebooks are grouped by purpose, not only by number.

| Group | Notebooks | Purpose |
|---|---|---|
| Setup | `00` | Confirm Python/R kernels and packages. |
| Foundation Python/R comparison | `01-06` | Learn enzyme activity, t-test, ANOVA, dose-response, gene expression, and Python/R reflection. |
| Advanced paired topics | `07-09` | IC50-style fitting, QC/outlier visualization, PCA/heatmap; Python and R versions are available. |
| Capstone | `10` | Combine dose-response ranking, QC, and cautious interpretation. |
| Visual showcase | `11` | Preview many graphical outputs; intentionally overlaps with later topics. |
| Reporting bridge | `13` | Generate structured, cautious summaries for AI-safe reporting practice. |
| Python-first applied lab topics | `14-20` | Experimental design, enzyme kinetics, standard curves, plate QC, qPCR, growth curves, and sequence basics. |
| AI and advancement tracks | `21-22` | AI/LLM summary review plus role-based career and academic portfolio scenarios. |

## Path A: Quick First Success

Best for students new to Python or R.

Notebooks:

```text
00_Setup_Check_Python.ipynb
01_Enzyme_Activity_Python.ipynb
```

## Path B: Python vs R Comparison

Best for students who have seen R in coursework.

Notebooks:

```text
01_Enzyme_Activity_Python.ipynb
01_Enzyme_Activity_R.ipynb
02_T_Test_Python.ipynb
02_T_Test_R.ipynb
03_ANOVA_Python.ipynb
03_ANOVA_R.ipynb
06_Python_vs_R_Reflection.ipynb
```

## Path C: Drug Response / BioDose Path

Best for students interested in drug testing or assay data.

Notebooks:

```text
04_Dose_Response_Python.ipynb
04_Dose_Response_R.ipynb
07_Advanced_IC50_Curve_Fitting_Python.ipynb
08_Advanced_Data_QC_Outlier_Visualization_Python.ipynb
10_Capstone_BioDose_Advanced_Challenge.ipynb
```

## Path D: Gene Expression / Bioinformatics Path

Best for students curious about computational biology.

Notebooks:

```text
05_Gene_Expression_Python.ipynb
05_Gene_Expression_R.ipynb
09_Advanced_PCA_Heatmap_Gene_Expression_Python.ipynb
09_Advanced_PCA_Heatmap_Gene_Expression_R.ipynb
```

## Recommended Starting Choice

Most students:

```text
Path A → Path B → then choose Path C or D
```

## Path E: Python-First Advanced Applied Lab Skills Path

Best for students who want practical lab-data topics beyond the first statistics notebooks. These are advanced extensions, not duplicate replacements for the foundations.

Notebooks:

```text
14_Experimental_Design_and_Replicates_Python.ipynb
15_Enzyme_Kinetics_Michaelis_Menten_Python.ipynb
16_Standard_Curve_Bradford_Assay_Python.ipynb
17_Assay_QC_Plate_Layout_Python.ipynb
18_qPCR_Delta_Delta_Ct_Python.ipynb
19_Growth_Curve_OD600_Python.ipynb
20_Sequence_Basics_GC_Content_Python.ipynb
21_AI_LLM_Lab_Summary_Review_Python.ipynb
22_Career_Academic_Advancement_Tracks_Python.ipynb
```

How these extend earlier topics:

| Notebook | Why it is advanced/applied | Earlier foundation it builds on |
|---|---|---|
| `14_Experimental_Design_and_Replicates_Python.ipynb` | Adds controls, replicate balance, SD vs SEM, and design review. | Enzyme activity summaries |
| `15_Enzyme_Kinetics_Michaelis_Menten_Python.ipynb` | Adds substrate concentration, saturation, Km, and Vmax. | Enzyme activity |
| `16_Standard_Curve_Bradford_Assay_Python.ipynb` | Adds calibration, unknown estimation, interpolation, and extrapolation checks. | Summary statistics and plotting |
| `17_Assay_QC_Plate_Layout_Python.ipynb` | Adds spatial QC, edge wells, and plate layout interpretation. | QC/outlier review |
| `18_qPCR_Delta_Delta_Ct_Python.ipynb` | Adds Ct, housekeeping normalization, delta-delta Ct, and relative expression. | Gene expression fold change |
| `19_Growth_Curve_OD600_Python.ipynb` | Adds time-course data, OD600, log-phase rate, and doubling time. | Grouped summaries and line plots |
| `20_Sequence_Basics_GC_Content_Python.ipynb` | Adds DNA string analysis, GC content, motifs, and reverse complements. | Intro gene/bioinformatics concepts |
| `21_AI_LLM_Lab_Summary_Review_Python.ipynb` | Adds AI/LLM review skills, claim-boundary checks, and safer scientific wording. | All interpretation and limitation sections |
| `22_Career_Academic_Advancement_Tracks_Python.ipynb` | Adds role-based synthetic scenarios for QC, research assistant, assay development, molecular biology, bioinformatics, and AI communication tracks. | Advanced applied notebooks and portfolio guides |

Note: `11_Graphical_Showcase_Python.ipynb` is a visual overview that intentionally reuses multiple topics. `13_BioDose_AI_Bridge_Python.ipynb` is an AI-safe reporting bridge for structured summaries, not a new wet-lab assay.

## Path F: Academic Advancement And Application Portfolio Path

Best for students preparing for master's applications, medical-school preparation, research assistant roles, summer research programs, or special academic programs.

Recommended notebooks:

```text
10_Capstone_BioDose_Advanced_Challenge.ipynb
14_Experimental_Design_and_Replicates_Python.ipynb
15_Enzyme_Kinetics_Michaelis_Menten_Python.ipynb
16_Standard_Curve_Bradford_Assay_Python.ipynb
18_qPCR_Delta_Delta_Ct_Python.ipynb
21_AI_LLM_Lab_Summary_Review_Python.ipynb
22_Career_Academic_Advancement_Tracks_Python.ipynb
```

Recommended companion guide:

```text
ADVANCEMENT_AND_PORTFOLIO_GUIDE.md
```

Suggested deliverable:

```text
one figure + one cautious result paragraph + one limitation + one next-step idea + one short reflection
```
