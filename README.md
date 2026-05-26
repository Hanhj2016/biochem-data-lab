# BioChem Data Lab

**A Python + R + Jupyter starter kit for Biochemistry and life science data analysis.**

BioChem Data Lab helps students practice small, visual, synthetic-data analyses across Biochemistry, molecular biology, assay QC, and intro bioinformatics. The focus is:

```text
Biochemistry question
→ dataset preview
→ analysis
→ graphical output
→ cautious interpretation
→ limitations
```

All datasets are synthetic and for learning only. Do not treat outputs as clinical, diagnostic, regulatory, drug-efficacy, or real biological evidence.

## Start Here

For the first session, open:

```text
START_HERE.md
```

For setup by platform, use:

```text
Setup_Guide/00_Quick_Start.md
Setup_Guide/01_Windows11_Setup.md
Setup_Guide/02_Ubuntu24_Setup.md
Setup_Guide/03_macOS_Setup.md
Setup_Guide/04_R_Kernel_IRkernel_Setup.md
Setup_Guide/05_Troubleshooting.md
Setup_Guide/06_Conda_Navigator_GUI_Guide.md
```

## Main Learning Guides

```text
Learning_Path_Chooser.md
STUDENT_PROJECT_MENU.md
WORKSHOP_PLAN.md
COMMON_MISTAKES.md
DATA_DISCLAIMER.md
AI_USE_GUIDE.md
GLOSSARY.md
ROADMAP.md
GITHUB_REPOSITORY_GUIDE.md
```

## Core Notebook Path

```text
notebooks/00_Setup_Check_Python.ipynb
notebooks/01_Enzyme_Activity_Python.ipynb
notebooks/02_T_Test_Python.ipynb
notebooks/03_ANOVA_Python.ipynb
notebooks/04_Dose_Response_Python.ipynb
notebooks/05_Gene_Expression_Python.ipynb
notebooks/06_Python_vs_R_Reflection.ipynb
```

Matching R notebooks are included for the early Python/R comparison path.

## Visual Showcase

To see the strongest graphical outputs first, open:

```text
notebooks/11_Graphical_Showcase_Python.ipynb
```

It exports interactive Plotly figures to:

```text
example_outputs/
```

## Extended Notebook Topics

Optional notebooks cover:

- data QC and outlier visualization
- IC50-style curve fitting
- heatmaps and PCA-style sample maps
- BioDose AI bridge logic
- experimental design and replicates
- enzyme kinetics
- Bradford-style standard curves
- 96-well plate QC
- qPCR delta-delta Ct
- OD600 growth curves
- sequence GC content and motif basics

Use `STUDENT_PROJECT_MENU.md` to choose a mini-project.

## Data and Teaching Support

Scenario datasets are documented here:

```text
data/SCENARIO_DATASETS_README.md
```

Teaching support folders:

```text
challenge_prompts/
expected_outputs/
writing_templates/
code_recipes/python/
code_recipes/r/
src/
R/
tests/
```

## Python Environment

Minimum Python setup:

```bash
conda create -n biochem-stats python=3.11 -y
conda activate biochem-stats
pip install pandas numpy scipy statsmodels plotly jupyter jupyterlab
jupyter notebook
```

For R notebooks, install R, IRkernel, and tidyverse. See `Setup_Guide/04_R_Kernel_IRkernel_Setup.md`.

## Tests

The Python helper functions have lightweight pytest coverage:

```bash
pip install pytest
pytest
```

## Repository

Recommended repository name:

```text
biochem-data-lab
```

Suggested description:

```text
A Python + R + Jupyter starter kit for Biochemistry and life science data analysis.
```
