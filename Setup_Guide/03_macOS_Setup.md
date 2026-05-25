# macOS Setup Guide

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

```bash
jupyter notebook
```

## R and IRkernel

Install R from CRAN. Then in R or RStudio:

```r
install.packages("IRkernel")
IRkernel::installspec()
install.packages("tidyverse")
```

Restart Jupyter.
