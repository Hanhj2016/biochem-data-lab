# Conda Navigator GUI Guide for Running the Python/R Notebooks

## Purpose

This guide shows how to run the Biochemistry Python/R comparison notebooks using **Anaconda / Conda Navigator GUI**, without relying mainly on command-line commands.

The command line is still useful later, but Conda Navigator is a comfortable first step.

---

# Part 1: Open Conda Navigator

## Windows 11

1. Click **Start Menu**.
2. Search for **Anaconda Navigator** or **Conda Navigator**.
3. Open it.

## Ubuntu 24.04

If Navigator is installed, open a terminal and run:

```bash
anaconda-navigator
```

If it is not installed in the base environment:

```bash
conda install anaconda-navigator
```

Then run:

```bash
anaconda-navigator
```

---

# Part 2: Create a New Environment

1. In Conda Navigator, click **Environments** on the left.
2. Click **Create**.
3. Name the environment:

```text
biochem-stats
```

4. Choose Python version:

```text
Python 3.11
```

5. Click **Create**.

This environment will be used for the Python notebooks.

---

# Part 3: Install Python Packages Using Navigator

1. Select the `biochem-stats` environment.
2. Change the package filter from **Installed** to **Not installed**.
3. Search and install these packages if available:

```text
pandas
numpy
scipy
statsmodels
plotly
jupyter
jupyterlab
```

4. Select packages and click **Apply**.

## If Some Packages Are Not Available

Some packages may be easier to install using the environment terminal.

In Navigator:

1. Select `biochem-stats`.
2. Click the small triangle / play button next to the environment name.
3. Choose **Open Terminal**.
4. Run:

```bash
pip install pandas numpy scipy statsmodels plotly jupyter jupyterlab
```

This is still launched from the GUI environment, so it is less confusing than opening a random terminal.

---

# Part 4: Launch Jupyter Notebook from Navigator

1. Go to **Home** in Navigator.
2. At the top, make sure the selected environment is:

```text
biochem-stats
```

3. Find **Jupyter Notebook**.
4. Click **Launch**.

A browser window should open.

---

# Part 5: Open the Downloaded Notebook Folder

In Jupyter Notebook:

1. Navigate to the extracted folder:

```text
biochem_r_python_notebook_comparison_advanced
```

2. Open the `notebooks/` folder.
3. Start with:

```text
00_Setup_Check_Python.ipynb
```

Then continue with:

```text
01_Enzyme_Activity_Python.ipynb
01_Enzyme_Activity_R.ipynb
...
```

---

# Part 6: Add R Kernel to Jupyter

The R notebooks require the R kernel, usually called **IRkernel**.

## Option A: If RStudio or R Console Is Available

Open R or RStudio and run:

```r
install.packages("IRkernel")
IRkernel::installspec()
install.packages("tidyverse")
```

Then restart Jupyter Notebook.

## Option B: From Conda Navigator Terminal

In Navigator:

1. Go to **Environments**.
2. Select the relevant environment.
3. Click the play/triangle button.
4. Choose **Open Terminal**.
5. Start R:

```bash
R
```

Then inside R:

```r
install.packages("IRkernel")
IRkernel::installspec()
install.packages("tidyverse")
```

Exit R:

```r
q()
```

Restart Jupyter Notebook.

---

# Part 7: Confirm R Kernel Works

Open:

```text
00_Setup_Check_R.ipynb
```

At the top-right of Jupyter Notebook, the kernel should show something like:

```text
R
```

Run the cells.

If `library(tidyverse)` works, the R notebook setup is ready.

---

# Part 8: If the R Kernel Does Not Show Up

Try:

1. Close Jupyter Notebook.
2. Reopen it from Conda Navigator.
3. Open `00_Setup_Check_R.ipynb`.
4. Go to:

```text
Kernel → Change Kernel
```

5. Look for:

```text
R
```

If it still does not show, run this again inside R:

```r
IRkernel::installspec(user = TRUE)
```

Then restart Jupyter.

---

# Part 9: Suggested GUI-Based Workflow

## First session

1. Open Conda Navigator.
2. Select `biochem-stats`.
3. Launch Jupyter Notebook.
4. Open:

```text
00_Setup_Check_Python.ipynb
```

5. Run all cells.

## Second session

1. Launch Jupyter Notebook from Navigator.
2. Open:

```text
00_Setup_Check_R.ipynb
```

3. Confirm R kernel works.

## Third session

Start paired learning:

```text
01_Enzyme_Activity_Python.ipynb
01_Enzyme_Activity_R.ipynb
```

Compare both versions.

---

# Part 10: Recommended Learning Order

```text
00_Setup_Check_Python.ipynb
00_Setup_Check_R.ipynb
01_Enzyme_Activity_Python.ipynb
01_Enzyme_Activity_R.ipynb
02_T_Test_Python.ipynb
02_T_Test_R.ipynb
03_ANOVA_Python.ipynb
03_ANOVA_R.ipynb
04_Dose_Response_Python.ipynb
04_Dose_Response_R.ipynb
05_Gene_Expression_Python.ipynb
05_Gene_Expression_R.ipynb
06_Python_vs_R_Reflection.ipynb
```

Advanced notebooks can be tried later:

```text
07_Advanced_IC50_Curve_Fitting_Python.ipynb
07_Advanced_IC50_Curve_Fitting_R.ipynb
08_Advanced_Data_QC_Outlier_Visualization_Python.ipynb
08_Advanced_Data_QC_Outlier_Visualization_R.ipynb
09_Advanced_PCA_Heatmap_Gene_Expression_Python.ipynb
09_Advanced_PCA_Heatmap_Gene_Expression_R.ipynb
10_Capstone_BioDose_Advanced_Challenge.ipynb
```

---

# Simple Troubleshooting

## Jupyter launches but cannot find files

Make sure Jupyter is opened in or navigated to the extracted project folder.

## Python package missing

In Conda Navigator:

```text
Environments → biochem-stats → Open Terminal
```

Then run:

```bash
pip install package_name
```

## R package missing

Open R and run:

```r
install.packages("package_name")
```

## Wrong kernel

In notebook:

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

---

# Suggested Student-Friendly Framing

The first goal is simply:

```text
Open a notebook.
Run cells.
See a table.
See a plot.
Compare Python and R for the same Biochemistry question.
```

That is enough for the first session.
