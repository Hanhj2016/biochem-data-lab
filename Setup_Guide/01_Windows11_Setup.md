# Windows 11 Setup Guide

## Recommended Path

Use Conda Navigator GUI first.

## Install Tools

- Miniconda or Anaconda
- Conda Navigator
- R
- Jupyter Notebook / JupyterLab
- Optional: RStudio
- Optional: Cursor or VS Code

## Create Environment with Conda Navigator

1. Open Conda Navigator.
2. Click Environments.
3. Click Create.
4. Name: `biochem-stats`
5. Choose Python 3.11.
6. Click Create.

## Install Python Packages

Select `biochem-stats`, then install:

```text
pandas
numpy
scipy
statsmodels
plotly
jupyter
jupyterlab
```

If needed, open the environment terminal and run:

```bash
pip install pandas numpy scipy statsmodels plotly jupyter jupyterlab
```

## Launch Jupyter Notebook

Home → select `biochem-stats` → Launch Jupyter Notebook.

Open:

```text
notebooks/00_Setup_Check_Python.ipynb
```

## R Kernel Setup

Open R or RStudio:

```r
install.packages("IRkernel")
IRkernel::installspec()
install.packages("tidyverse")
```

Restart Jupyter and open:

```text
notebooks/00_Setup_Check_R.ipynb
```
