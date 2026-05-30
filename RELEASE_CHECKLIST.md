# Release Checklist

Use this before sharing BioChem Data Lab with students, instructors, or program reviewers.

## Documentation

- [ ] `README.md` points to `START_HERE.md` and `DOCUMENTATION_INDEX.md`.
- [ ] `DOCUMENTATION_INDEX.md` points to the current main guides.
- [ ] `Learning_Path_Chooser.md` explains notebook groups and paths.
- [ ] `STUDENT_PROJECT_MENU.md` lists current challenge and advancement options.
- [ ] `BILINGUAL_CONCEPT_GUIDE.md` covers the current notebook topics.
- [ ] Duplicate root-level guidance is consolidated into `ADVANCEMENT_AND_PORTFOLIO_GUIDE.md`.

## Notebook Readiness

- [ ] Core Python notebooks open: `00-05`.
- [ ] Core R comparison notebooks open where included: `00-05`, `07-09`.
- [ ] Python advanced notebooks open: `07-11`, `13-22`.
- [ ] Plotly notebooks include a renderer setup or fallback comment.
- [ ] Notebooks use relative paths from the `notebooks/` directory.
- [ ] Each teaching notebook includes a question, dataset preview, visual output, interpretation practice, and limitations.

## Data And Outputs

- [ ] Every notebook dataset path exists.
- [ ] Scenario datasets are documented in `data/SCENARIO_DATASETS_README.md`.
- [ ] Challenge prompts exist for scenario datasets intended as student projects.
- [ ] Expected learning points exist for supported challenges.
- [ ] Example outputs in `example_outputs/` are current enough for preview use.

## Code And Tests

- [ ] Reusable Python helpers are in `src/`.
- [ ] Code recipes run from the repository root.
- [ ] `pytest` passes or known warnings are documented.
- [ ] New helper functions have focused tests.

## Scientific Boundaries

- [ ] All student-facing docs state that data are synthetic.
- [ ] No file presents outputs as clinical, diagnostic, regulatory, drug-efficacy, or real biological evidence.
- [ ] AI/LLM examples are framed as draft review and communication support, not scientific authority.
- [ ] Outlier language says review/flag rather than automatic deletion.
- [ ] Medical-school and career framing emphasizes reasoning, evidence boundaries, and communication.

## Final Student Artifact Check

A strong artifact should include:

```text
one figure or table
one cautious interpretation
one data quality note
one limitation
one next-step idea
one short reflection
```
