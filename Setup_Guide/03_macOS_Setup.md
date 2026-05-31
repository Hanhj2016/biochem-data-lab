# macOS Setup Guide

## Recommended Path

Use Terminal. Start Jupyter from the BioChem Data Lab project folder so relative paths like `../data/...` work correctly.

## Supported

- macOS Intel
- macOS Apple Silicon: M1, M2, M3, M4

For Apple Silicon, use an Apple Silicon compatible Conda installer when possible.

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
cd ~/Documents/biochem-data-lab
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

## R and IRkernel

Install R from CRAN. Then in R or RStudio:

```r
install.packages("IRkernel")
IRkernel::installspec()
install.packages("tidyverse")
```

Restart Jupyter and open:

```text
notebooks/00_Setup_Check_R.ipynb
```
