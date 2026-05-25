# Ubuntu 24.04 Setup Guide

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

## Optional Conda Navigator

```bash
conda install anaconda-navigator
anaconda-navigator
```

## R and IRkernel

```bash
sudo apt update
sudo apt install r-base
R
```

Inside R:

```r
install.packages("IRkernel")
IRkernel::installspec()
install.packages("tidyverse")
q()
```

Restart Jupyter.
