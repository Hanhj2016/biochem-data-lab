# R Kernel / IRkernel Setup Guide

## Install

Open R or RStudio:

```r
install.packages("IRkernel")
IRkernel::installspec()
install.packages("tidyverse")
```

## Check

Restart Jupyter and open:

```text
notebooks/00_Setup_Check_R.ipynb
```

The kernel should show `R`.

## If R Kernel Is Missing

```r
IRkernel::installspec(user = TRUE)
```

Restart Jupyter.
