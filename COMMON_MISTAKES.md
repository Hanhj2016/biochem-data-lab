# Common Mistakes and Quick Fixes

## 1. Jupyter opens in the wrong folder

Make sure you are inside the BioChem Data Lab folder.

You should see:

```text
README.md
data/
notebooks/
Setup_Guide/
```

## 2. Wrong notebook kernel

In Jupyter:

```text
Kernel → Change Kernel
```

Choose:

```text
Python 3
```

or:

```text
R
```

## 3. Python package not installed

Open the `biochem-stats` environment terminal and run:

```bash
pip install package_name
```

Example:

```bash
pip install plotly
```

## 4. R kernel does not show up

Open R or RStudio and run:

```r
install.packages("IRkernel")
IRkernel::installspec(user = TRUE)
```

Restart Jupyter.

## 5. CSV path error

If a notebook cannot find a CSV file, check that the notebook path uses:

```text
../data/...
```

Most notebooks are inside the `notebooks/` folder, so `../data/` means “go up one folder, then enter data.”

## 6. Forgot to run previous cells

If a variable is not defined, run cells from the top.

In Jupyter:

```text
Kernel → Restart & Run All
```

## 7. Confusing SD and SEM

```text
SD = variability among observations
SEM = uncertainty around the estimated mean
```

Both are useful, but they do not mean the same thing.

## 8. Overinterpreting p-values

A small p-value does not automatically mean the biological effect is important.

Always consider:

```text
sample size
effect size
experimental design
biological relevance
data quality
```

## 9. Log scale with zero concentration

A log scale cannot display zero.

For dose-response plots, zero concentration is often plotted at a small placeholder value for visualization, such as:

```text
0.001
```

The notebook should clearly label this.

## 10. Treating synthetic data as real data

All sample datasets are synthetic and for learning.

Do not use them for scientific, clinical, or regulatory conclusions.

## 11. Removing outliers too quickly

A suspicious point should be reviewed, not automatically removed.

Check:

```text
raw data
lab notes
instrument notes
replicate pattern
possible sample handling issue
```

## 12. R package install asks for mirror

Choose a nearby CRAN mirror.

For Canada, any North American mirror is usually fine.

## 13. Plot does not appear

Try:

```text
Kernel → Restart Kernel
```

Then run all cells again.

## 14. Notebook is too hard

Start with:

```text
01_Enzyme_Activity_Python.ipynb
```

Then return to advanced notebooks later.
