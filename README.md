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

For the first session, open [START_HERE.md](START_HERE.md).

For setup by platform, use:

- [Quick Start](Setup_Guide/00_Quick_Start.md)
- [Windows 11 Setup](Setup_Guide/01_Windows11_Setup.md)
- [Ubuntu 24.04 Setup](Setup_Guide/02_Ubuntu24_Setup.md)
- [macOS Setup](Setup_Guide/03_macOS_Setup.md)
- [R Kernel / IRkernel Setup](Setup_Guide/04_R_Kernel_IRkernel_Setup.md)
- [Troubleshooting](Setup_Guide/05_Troubleshooting.md)
- [Conda Navigator GUI Guide](Setup_Guide/06_Conda_Navigator_GUI_Guide.md)

## Main Learning Guides

Start with [DOCUMENTATION_INDEX.md](DOCUMENTATION_INDEX.md) if you are unsure which guide to open.

Core student guides:

- [Learning Path Chooser](Learning_Path_Chooser.md)
- [Student Project Menu](STUDENT_PROJECT_MENU.md)
- [Bilingual Concept Guide](BILINGUAL_CONCEPT_GUIDE.md)
- [Advancement and Portfolio Guide](ADVANCEMENT_AND_PORTFOLIO_GUIDE.md)
- [Common Mistakes](COMMON_MISTAKES.md)
- [Data Disclaimer](DATA_DISCLAIMER.md)
- [AI Use Guide](AI_USE_GUIDE.md)
- [Glossary](GLOSSARY.md)

Instructor, setup, and sharing guides:

- [Workshop Plan](WORKSHOP_PLAN.md)
- [Roadmap](ROADMAP.md)
- [GitHub Repository Guide](GITHUB_REPOSITORY_GUIDE.md)
- [Release Checklist](RELEASE_CHECKLIST.md)
- [Setup Guides](Setup_Guide/00_Quick_Start.md)


## Notebook Numbering At A Glance

| Range | Role |
|---|---|
| `00` | Setup checks |
| `01-06` | Foundation Python/R comparison path |
| `07-09` | Advanced paired analysis topics |
| `10` | Capstone challenge |
| `11` | Graphical showcase, intentionally overlapping as a visual tour |
| `13` | AI-safe reporting bridge |
| `14-20` | Applied lab-data topics with Python and R notebooks |
| `21-22` | AI literacy plus career/academic advancement tracks |

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

Matching R notebooks are included for the early Python/R comparison path and for applied lab notebooks `14-20`. AI/reporting and career-track notebooks remain Python-first unless an R counterpart is listed.

## Visual Showcase

This notebook intentionally overlaps with several later topics. It is a visual tour, not a duplicate lesson. To see the strongest graphical outputs first, open:

```text
notebooks/11_Graphical_Showcase_Python.ipynb
```

It exports interactive Plotly figures to:

```text
example_outputs/
```

## Advanced and Applied Extension Topics

These notebooks extend the foundations rather than repeat them. Applied lab notebooks `14-20` now include both Python and R versions for university lab-data contexts. Optional notebooks cover:

- data QC and outlier visualization
- IC50-style curve fitting
- heatmaps and PCA-style sample maps
- BioDose AI bridge logic
- experimental design and replicates, extending enzyme activity into study-design thinking
- enzyme kinetics, extending enzyme activity into Michaelis-Menten saturation curves
- Bradford-style standard curves, adding protein concentration calibration
- 96-well plate QC, extending QC into spatial plate-layout effects
- qPCR delta-delta Ct, extending gene expression into method-specific normalization
- OD600 growth curves, adding microbial time-course analysis
- sequence GC content and motif basics, adding introductory bioinformatics
- AI/LLM lab-summary review, adding human-in-the-loop scientific communication practice
- career and academic advancement tracks, adding role-based synthetic lab scenarios and portfolio outputs

Use [STUDENT_PROJECT_MENU.md](STUDENT_PROJECT_MENU.md) to choose a mini-project.

## Data and Teaching Support

Scenario datasets are documented in [data/SCENARIO_DATASETS_README.md](data/SCENARIO_DATASETS_README.md).

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

For R notebooks, install R, IRkernel, and tidyverse. See [Setup_Guide/04_R_Kernel_IRkernel_Setup.md](Setup_Guide/04_R_Kernel_IRkernel_Setup.md). R helper modules include applied lab functions in `R/` for enzyme kinetics, standard curves, plate QC, qPCR, growth curves, and sequence basics.

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
