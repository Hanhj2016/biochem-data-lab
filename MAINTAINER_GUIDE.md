# Maintainer Guide

Use this guide for workshop planning, release checks, and future direction. Student-facing navigation lives in [START_HERE.md](START_HERE.md), [Learning_Path_Chooser.md](Learning_Path_Chooser.md), and [DOCUMENTATION_INDEX.md](DOCUMENTATION_INDEX.md).

All datasets and outputs remain synthetic and educational. Do not frame them as clinical, diagnostic, regulatory, drug-efficacy, or real biological evidence.

---

## Release Checklist

Use this before sharing BioChem Data Lab with students, instructors, or program reviewers.

### Documentation

- [ ] `README.md` points to `START_HERE.md` and `DOCUMENTATION_INDEX.md`.
- [ ] `DOCUMENTATION_INDEX.md` points to the current main guides.
- [ ] `Learning_Path_Chooser.md` explains notebook groups, learning paths, project options, and challenge choices.
- [ ] `BILINGUAL_CONCEPT_GUIDE.md` covers current notebook topics, key terms, common mistakes, and synthetic data boundaries.
- [ ] Duplicate root-level guidance is consolidated into the main guides.

### Notebook Readiness

- [ ] Core Python notebooks open: `00-05`.
- [ ] Core R comparison notebooks open where included: `00-05`, `07-09`, `14-20`.
- [ ] Applied R notebooks open and compare cleanly with the Python versions: `14-20`.
- [ ] Python advanced notebooks open: `07-11`, `13-22`.
- [ ] Plotly notebooks include a renderer setup or fallback comment.
- [ ] Notebooks use relative paths from the `notebooks/` directory.
- [ ] Each teaching notebook includes a question, dataset preview, visual output, interpretation practice, and limitations.

### Data And Outputs

- [ ] Every notebook dataset path exists.
- [ ] Scenario datasets are documented in `data/SCENARIO_DATASETS_README.md`.
- [ ] Challenge prompts exist for scenario datasets intended as student projects.
- [ ] Expected learning points exist for supported challenges.
- [ ] Generated HTML outputs are either regenerated locally or intentionally ignored by Git.

### Code And Tests

- [ ] Reusable Python helpers are in `src/`.
- [ ] Reusable R helpers are in `R/` where useful.
- [ ] Code recipes run from the repository root.
- [ ] `pytest` passes or known warnings are documented.
- [ ] New helper functions have focused tests.

### Scientific Boundaries

- [ ] All student-facing docs state that data are synthetic.
- [ ] No file presents outputs as clinical, diagnostic, regulatory, drug-efficacy, or real biological evidence.
- [ ] AI/LLM examples are framed as draft review and communication support, not scientific authority.
- [ ] Outlier language says review/flag rather than automatic deletion.
- [ ] Medical-school and career framing emphasizes reasoning, evidence boundaries, and communication.

### Final Student Artifact Check

A strong artifact should include:

```text
one figure or table
one cautious interpretation
one data quality note
one limitation
one next-step idea
one short reflection
```

---

## Workshop Plan

### Purpose

This section helps mentors, parents, or teachers use BioChem Data Lab in a short workshop or study session.

Recommended approach:

```text
1. Start with one Python notebook.
2. Let the student run the cells.
3. Focus on the figure and interpretation.
4. Then show the matching R notebook if useful.
5. Ask which version feels clearer.
6. Let the student choose the next path.
```

Start with:

```text
small synthetic data
one table
one plot
one interpretation
```

Avoid starting with:

```text
large real datasets
full RNA-seq pipelines
advanced statistics
deployment
complex project structure
```

### 60-Minute Workshop

Goal: run one Python notebook and understand one scientific figure.

```text
0-10 min: setup check
10-25 min: enzyme activity Python notebook
25-40 min: chart and summary statistics
40-50 min: write interpretation
50-60 min: discussion and next path
```

Notebook: `notebooks/01_Enzyme_Activity_Python.ipynb`

Discussion questions:

```text
What is the biological question?
What is the control group?
What is the treatment group?
What does the bar chart show?
What are the limitations?
```

### 90-Minute Python vs R Comparison

Goal: compare Python and R for the same Biochemistry dataset.

```text
0-10 min: Python setup check
10-30 min: enzyme activity Python notebook
30-50 min: enzyme activity R notebook
50-70 min: compare outputs
70-90 min: reflection
```

Notebooks:

```text
notebooks/01_Enzyme_Activity_Python.ipynb
notebooks/01_Enzyme_Activity_R.ipynb
notebooks/06_Python_vs_R_Reflection.ipynb
```

### 2-Hour Drug Response Session

Goal: explore dose-response data and create an interactive figure.

```text
0-15 min: setup and dataset overview
15-45 min: dose-response Python notebook
45-70 min: dose-response R notebook
70-95 min: QC / outlier visualization
95-120 min: interpretation and next experiment
```

Notebooks:

```text
notebooks/04_Dose_Response_Python.ipynb
notebooks/04_Dose_Response_R.ipynb
notebooks/08_Advanced_Data_QC_Outlier_Visualization_Python.ipynb
```

Suggested workshop rule:

```text
one dataset
one plot
one interpretation
one next question
```

---

## Roadmap

### Phase 1: Python/R Notebook Comparison

Current focus:

```text
Jupyter notebooks
Python vs R comparison
basic Biochemistry statistics
synthetic datasets
visual figures
```

### Phase 2: Richer Scenario Datasets

Added or planned:

```text
enzyme activity scenarios
drug response scenarios
gene expression scenarios
enzyme kinetics scenarios
standard curve scenarios
plate QC scenarios
qPCR scenarios
growth curve scenarios
synthetic sequence scenarios
fictional literature abstracts
career and academic advancement scenarios
expected outputs
challenge prompts
```

### Phase 3: BioDose AI

Added foundation or possible future project:

```text
Gradio app
drug response upload
interactive Plotly chart
data quality score
AI explanation
figure caption generator
mini report
AI/LLM lab-summary review
AI figure-caption review
```

### Phase 4: Quarto Reports

Possible future project:

```text
HTML reports
mini posters
academic interpretation
figure captions
study notes
```

### Phase 5: Additional Bio-AI Projects

Possible future modules:

```text
ProteinLens
TargetReader AI
GeneShift
BioBridge AI Lab
```

### Phase 6: Sharing and Portfolio

Possible future improvements:

```text
GitHub Pages
screenshots
demo GIF
student showcase examples
workshop version
```

### Guiding Principle

Keep each step:

```text
small
visual
Biochemistry-connected
student-friendly
easy to start
```
