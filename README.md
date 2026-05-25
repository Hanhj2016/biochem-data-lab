# Biochemistry Statistics: Python vs R Jupyter Notebook Comparison

## Purpose

This starter package helps a Biochemistry student compare **Python** and **R** on the same academic life science / biochemistry statistics use cases.

The goal is to see how each language feels for:

- reading data
- summarizing lab measurements
- doing basic statistics
- visualizing results
- writing cautious academic interpretation
- preparing for AI-assisted bioinformatics projects such as BioDose AI

## How to Run

```bash
conda create -n biochem-stats python=3.11 -y
conda activate biochem-stats
pip install pandas numpy scipy statsmodels plotly jupyter jupyterlab
jupyter notebook
```

For R kernel support, make sure R and IRkernel are installed. Inside R:

```r
install.packages("IRkernel")
IRkernel::installspec()
install.packages("tidyverse")
```

Then restart Jupyter Notebook.


---

## Conda Navigator GUI Option

A GUI-based setup guide is included:

```text
Conda_Navigator_GUI_Guide.md
```

This guide explains how to:

- create the `biochem-stats` environment using Conda Navigator
- install packages from the Navigator GUI
- open an environment terminal if needed
- launch Jupyter Notebook from Navigator
- register and use the R kernel / IRkernel
- open the Python and R notebooks

### Quick GUI Workflow

1. Open **Conda Navigator**.
2. Go to **Environments**.
3. Create a new environment named:

```text
biochem-stats
```

4. Choose Python 3.11.
5. Install or confirm these packages:

```text
pandas
numpy
scipy
statsmodels
plotly
jupyter
jupyterlab
```

6. Go to **Home**.
7. Select the `biochem-stats` environment.
8. Launch **Jupyter Notebook**.
9. Open the `notebooks/` folder.
10. Start with:

```text
00_Setup_Check_Python.ipynb
```

For R notebooks, install and register IRkernel in R:

```r
install.packages("IRkernel")
IRkernel::installspec()
install.packages("tidyverse")
```

Then restart Jupyter and open:

```text
00_Setup_Check_R.ipynb
```

## Suggested Order

1. `00_Setup_Check_Python.ipynb`
2. `00_Setup_Check_R.ipynb`
3. `01_Enzyme_Activity_Python.ipynb`
4. `01_Enzyme_Activity_R.ipynb`
5. `02_T_Test_Python.ipynb`
6. `02_T_Test_R.ipynb`
7. `03_ANOVA_Python.ipynb`
8. `03_ANOVA_R.ipynb`
9. `04_Dose_Response_Python.ipynb`
10. `04_Dose_Response_R.ipynb`
11. `05_Gene_Expression_Python.ipynb`
12. `05_Gene_Expression_R.ipynb`
13. `06_Python_vs_R_Reflection.ipynb`

## Connection to BioDose AI

After these notebooks, the next step is:

```text
Python dose-response notebook
→ reusable Python functions
→ Gradio app
→ OpenAI API explanation
→ Quarto report
```

## Academic Boundary

The datasets are synthetic and designed for learning. Do not treat the results as real biological conclusions.


---

# Advanced / Challenging Notebooks

These notebooks are optional extensions after the basic Python/R comparison notebooks.

They add more graphical representation and industry-inspired thinking while staying beginner-friendly.

## Added Notebooks

| Notebook | Language | Topic |
|---|---|---|
| `07_Advanced_IC50_Curve_Fitting_Python.ipynb` | Python | IC50-style logistic curve fitting |
| `07_Advanced_IC50_Curve_Fitting_R.ipynb` | R | IC50-style logistic curve fitting |
| `08_Advanced_Data_QC_Outlier_Visualization_Python.ipynb` | Python | data quality and outlier visualization |
| `08_Advanced_Data_QC_Outlier_Visualization_R.ipynb` | R | data quality and outlier visualization |
| `09_Advanced_PCA_Heatmap_Gene_Expression_Python.ipynb` | Python | heatmap and PCA-style gene expression visualization |
| `09_Advanced_PCA_Heatmap_Gene_Expression_R.ipynb` | R | heatmap and PCA-style gene expression visualization |
| `10_Capstone_BioDose_Advanced_Challenge.ipynb` | Python | feature design challenge for BioDose AI |

## Recommended Advanced Learning Order

1. Data QC / outlier visualization
2. IC50-style curve fitting
3. Gene expression heatmap and PCA
4. Capstone BioDose feature design

## Academic Boundary

These are learning notebooks with synthetic data.

Do not treat IC50 estimates, gene clusters, or outlier flags as real biological conclusions.
