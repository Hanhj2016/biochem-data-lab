# Troubleshooting Guide

## Jupyter opens in the wrong folder

Navigate to the extracted starter kit folder. You should see `data/`, `notebooks/`, and `README.md`.

## Python package missing

Open the `biochem-stats` environment terminal:

```bash
pip install package_name
```

## R package missing

Open R:

```r
install.packages("package_name")
```

## R kernel missing

Open R:

```r
IRkernel::installspec(user = TRUE)
```

Restart Jupyter.

## Wrong kernel selected

In notebook:

```text
Kernel → Change Kernel
```

Choose Python 3 or R.
