# AGENTS.md

## Project

- Project name: BioChem Data Lab
- Repository name: biochem-data-lab
- Purpose: Python + R + Jupyter starter kit for Biochemistry and life science students.

## General Guidance

1. Keep tutorials student-friendly and Biochemistry-first.
2. Avoid wording that implies students need to be pushed, pressured, or motivated.
3. Use synthetic datasets only.
4. Do not make clinical, medical, drug efficacy, regulatory, or diagnostic claims.
5. Keep notebooks beginner-friendly, with optional challenge sections for extension work.
6. Prefer robust, readable beginner-friendly code over clever code.
7. After changes, update README files or setup guides when the user-facing workflow changes.

## Notebook Expectations

Every notebook should include:

- Biochemistry question
- Dataset preview
- Analysis steps
- Graphical output
- Interpretation practice
- Limitations
- Python/R comparison questions when relevant

## Python Guidance

- Use `pandas`, `numpy`, `scipy`, `statsmodels`, and `plotly`.
- Keep reusable functions in `src/`.
- Avoid hard-coded absolute paths.
- Use clear variable names and short, direct comments where helpful for beginners.

## R Guidance

- Use `tidyverse` and `ggplot2`.
- Avoid fragile dependencies when simple base R works.
- Avoid `column_to_rownames()` unless `tibble` is explicitly loaded.
- Keep examples readable for students comparing R with Python.

## Data and Interpretation Boundaries

- All datasets should be synthetic and educational.
- Do not present outputs as real biological, clinical, medical, diagnostic, regulatory, or drug-efficacy evidence.
- Use cautious scientific language such as "suggests", "is consistent with", and "additional validation would be needed."
