# Ubuntu 24.04 Setup Guide

## Recommended Path

Use Terminal. Start Jupyter from the BioChem Data Lab project folder so relative paths like `../data/...` work correctly.

## Create Environment

```bash
conda create -n biochem-stats python=3.11 -y
conda activate biochem-stats
```

## Install Packages

```bash
pip install pandas numpy scipy statsmodels plotly jupyter jupyterlab
```

## Launch Jupyter

First change directory to the BioChem Data Lab project folder.

Example:

```bash
cd ~/workspace/biochem-data-lab
```

Then launch Jupyter:

```bash
jupyter notebook
```

When Jupyter opens in the browser, open:

```text
notebooks/00_Setup_Check_Python.ipynb
```

If the notebook cannot find a CSV file, check that Jupyter was started from the project root folder.

## Optional Conda Navigator

```bash
conda install anaconda-navigator
anaconda-navigator
```

## R and IRkernel

```bash
sudo apt update
sudo apt install -y r-base
R
```

Inside R:

```r
install.packages("IRkernel")
IRkernel::installspec()
install.packages("tidyverse")
q()
```

Restart Jupyter and open:

```text
notebooks/00_Setup_Check_R.ipynb
```
