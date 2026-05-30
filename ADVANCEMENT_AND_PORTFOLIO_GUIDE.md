# Advancement and Portfolio Guide

This consolidated guide covers career/job preparation, industry and lab reality, academic advancement, portfolio artifacts, and AI/LLM career literacy for BioChem Data Lab.

All project data are synthetic and educational. Use these materials to demonstrate scientific reasoning, reproducible analysis, visualization, quality review, and cautious communication. Do not present notebook outputs as clinical, diagnostic, regulatory, drug-efficacy, hiring, salary, or real biological evidence.

## Quick Use

For one strong student artifact, prepare:

```text
one figure or table
+ one cautious result paragraph
+ one data quality or uncertainty note
+ one limitation
+ one next-step idea
+ one short reflection
```

Good starting notebooks:

```text
10_Capstone_BioDose_Advanced_Challenge.ipynb
14_Experimental_Design_and_Replicates_Python.ipynb
15_Enzyme_Kinetics_Michaelis_Menten_Python.ipynb
16_Standard_Curve_Bradford_Assay_Python.ipynb
18_qPCR_Delta_Delta_Ct_Python.ipynb
21_AI_LLM_Lab_Summary_Review_Python.ipynb
22_Career_Academic_Advancement_Tracks_Python.ipynb
```

## Role And Academic Goal Map

| Goal or role | Useful notebooks | Skill demonstrated | Possible artifact |
|---|---|---|---|
| Master's or research master's preparation | `09`, `10`, `14`, `15`, `16`, `18`, `21`, `22` | quantitative reasoning, reproducible analysis, cautious scientific writing | one-page project summary |
| Medical-school preparation | `02`, `03`, `08`, `14`, `17`, `21`, `22` | evidence evaluation, controls, uncertainty, ethical interpretation boundaries | evidence-and-limitation reflection |
| Summer research or special program | `10`, `11`, `15`, `16`, `18`, `19`, `20`, `22` | independent mini-project thinking and figure-based communication | poster-style mini report |
| Research assistant | `01`, `14`, `15`, `22` | controls, replicates, enzyme activity, design review | replicate summary with design note |
| Lab technician | `14`, `16`, `17`, `22` | replicate handling, calibration, plate maps, QC review | standard curve or plate QC note |
| QC analyst | `08`, `16`, `17`, `22` | outlier review, acceptance-range thinking, edge-effect checks | QC table with flagged observations |
| Assay development associate | `04`, `07`, `10`, `15`, `17`, `22` | dose-response summaries, model caution, day-to-day robustness | dose-response or kinetics mini-report |
| Molecular biology student | `05`, `09`, `18`, `20`, `22` | expression summaries, heatmaps, PCA, qPCR normalization, sequence basics | qPCR or gene-expression interpretation paragraph |
| Bioinformatics beginner | `09`, `20`, `22`, `code_recipes/python/16_sequence_basics_python.py` | matrix thinking, PCA intuition, DNA string analysis | GC-content and motif summary |
| Scientific data communicator | `11`, `13`, `21`, `22` | figure choice, cautious language, AI-assisted summaries, human review | figure caption and AI-reviewed summary |

## Notebook 22 Role Tracks

`notebooks/22_Career_Academic_Advancement_Tracks_Python.ipynb` gives hands-on code and datasets for practical role scenarios:

| Track | Dataset | Practice focus |
|---|---|---|
| QC analyst | `data/career_scenarios/qc_plate_batch_review.csv` | plate-batch review and control-range checks |
| Research assistant | `data/career_scenarios/research_assistant_replicate_log.csv` | replicate balance and missing-replicate review |
| Assay development | `data/career_scenarios/assay_development_day_variability.csv` | day-to-day robustness checks |
| Molecular biology lab | `data/career_scenarios/molecular_biology_qpcr_review.csv` | qPCR Ct replicate QC |
| Bioinformatics assistant | `data/career_scenarios/bioinformatics_sequence_triage.csv` | sequence triage, GC content, motifs, ambiguous bases |
| AI scientific communication | `data/career_scenarios/ai_figure_caption_review.csv` | AI caption overclaim review and safer rewriting |

Challenge briefs and expected learning points are in `challenge_prompts/` and `expected_outputs/`.

## Industry And Lab Reality Checks

Before writing a conclusion, ask:

```text
Could this pattern come from assay setup, sample handling, instrument limits, plate position, data processing, missing controls, or batch effects?
```

| Topic | Lab reality check | Why it matters |
|---|---|---|
| Enzyme activity | Confirm control behavior, replicate consistency, and assay timing. | A lower mean is easier to trust when baseline behavior is stable. |
| t-test / ANOVA | Check sample size, group balance, outliers, and assumptions. | A p-value does not explain mechanism or practical importance. |
| Dose-response | Review concentration range, replicate spread, and log-scale plotting. | Curve shape depends on data quality and dose selection. |
| IC50-style fitting | Inspect coverage, residuals, bounds, and rerun needs. | Fitted parameters can look precise even when the assay is fragile. |
| QC outliers | Treat flags as review prompts, not automatic deletion rules. | Removing data requires documented reasoning. |
| Gene expression | Check normalization, batch effects, and replicate structure. | Fold change alone does not prove biological role. |
| PCA / heatmap | Confirm sample labels, scaling choices, and data quality. | Visual clustering can reflect biology, batch, or preprocessing. |
| Bradford standard curve | Check blank correction, linear range, dilution factor, and unknowns outside range. | Unknowns above the highest standard are usually diluted and rerun. |
| Plate layout QC | Review plate map, edge wells, row/column bias, and controls. | Spatial effects can mimic treatment differences. |
| qPCR | Review primer efficiency, melt curves, no-template controls, and housekeeping stability. | Raw Ct values should not be interpreted without normalization checks. |
| OD600 growth curve | Check blank correction, instrument range, culture metadata, and selected growth window. | Growth rate depends strongly on the time window chosen. |
| Sequence basics | Check sequence source, orientation, quality, and annotation context. | Short motifs do not prove biological function. |
| AI summaries | Keep source data traceable and review AI-written text. | AI can help explain; it should not invent claims. |

## What Real Teams Often Document

- dataset version or file name
- instrument, notebook, or script used
- control behavior
- replicate count and exclusions
- QC flags or reruns
- plotting choices
- analysis limitations
- reviewer comments or next steps

## Application-Ready Artifact Structure

```text
Project title
Biochemistry question
Dataset used
Methods in 2-4 sentences
One figure or summary table
Main observation
Data quality or uncertainty note
Limitation
Suggested next experiment or analysis
Short reflection on what the project taught you
```

Recommended templates:

```text
writing_templates/academic_project_summary_template.md
writing_templates/application_reflection_template.md
writing_templates/academic_interview_prep_template.md
writing_templates/figure_caption_template.md
writing_templates/results_paragraph_template.md
writing_templates/limitations_template.md
writing_templates/next_experiment_template.md
```

## Strong Artifact Rubric

| Criterion | Good evidence |
|---|---|
| Biological question | States the question in plain language. |
| Dataset understanding | Names the dataset and key columns. |
| Analysis clarity | Explains the calculation or graph without overcomplication. |
| Figure quality | Uses a plot that matches the question. |
| Interpretation | Describes the observed pattern cautiously. |
| QC awareness | Mentions replicates, uncertainty, range, or flags. |
| Limitation | States what the synthetic data cannot prove. |
| Next step | Suggests a reasonable follow-up check or analysis. |

## Academic Framing

For medical-school preparation, avoid presenting notebooks as clinical work. A stronger framing is:

```text
This project helped me practice interpreting biological data, evaluating uncertainty, and avoiding claims beyond the evidence.
```

For research programs, focus on method and reasoning:

```text
I used a synthetic biochemistry dataset to summarize replicate measurements, visualize the main trend, and write a cautious interpretation with limitations and a proposed next experiment.
```

Interview questions to practice:

1. What biological question did the notebook ask?
2. What columns were in the dataset, and what did they mean?
3. Why was this graph or statistical test used?
4. What is the main observation?
5. What is one limitation of the dataset or analysis?
6. What would you check before trusting this result in a real lab?
7. What would be a reasonable next experiment or analysis?
8. How would you explain the result to someone outside biochemistry?

## Career-Friendly Skill Phrases

Use these only when they honestly match completed work:

- Built beginner-friendly Python notebooks for synthetic biochemistry datasets.
- Summarized enzyme activity, cell viability, qPCR, OD600 growth, and sequence-summary data.
- Created Plotly visualizations with error bars and cautious interpretation notes.
- Practiced assay QC concepts including outlier review, plate edge effects, calibration range checks, and day-to-day review.
- Used synthetic sequence data to calculate GC content, motif counts, and ambiguous-base review flags.
- Reviewed AI-style scientific captions or summaries for unsupported claims and safer wording.

## AI And LLM Career Literacy

Life-science students increasingly benefit from a hybrid skill set:

```text
biology domain understanding
+ data analysis
+ visualization
+ quality control
+ cautious scientific writing
+ AI/LLM literacy
```

LLMs can help with:

- explaining code in plain language
- drafting figure captions
- converting notes into structured summaries
- creating checklists
- comparing alternative interpretations
- translating technical ideas for different audiences
- generating table-style or structured report outputs when guided clearly

LLMs should not be used to:

- invent data
- hide uncertainty
- delete outliers without review
- claim mechanism from synthetic data
- make clinical, diagnostic, regulatory, or drug-efficacy conclusions
- replace instructor, supervisor, or domain-expert review

AI-safe notebook workflow:

```text
1. Run the notebook yourself.
2. Identify the dataset, figure, and main observation.
3. Write the limitation in your own words.
4. Ask AI to improve clarity, not to invent a conclusion.
5. Check every statement against the notebook output.
6. Keep the synthetic-data disclaimer.
```

For practical AI prompt examples, see `AI_USE_GUIDE.md`.

## Cautious Wording

Use wording like:

- “In this synthetic dataset...”
- “The pattern is consistent with...”
- “This point should be reviewed before interpretation.”
- “The estimate is outside the standard curve range.”
- “A real workflow would need protocol details, controls, and validation.”

Avoid wording like:

- “This proves...”
- “This drug is effective...”
- “This biomarker diagnoses...”
- “This synthetic dataset proves a mechanism.”

## Sources For AI/Career Trend Awareness

These are broad trend references, not promises for any individual job market:

- U.S. Bureau of Labor Statistics, Occupational Outlook Handbook. https://www.bls.gov/ooh/
- World Economic Forum, Future of Jobs Report 2025. https://www.weforum.org/publications/the-future-of-jobs-report-2025/
- OpenAI API documentation: Text generation and Structured Outputs. https://platform.openai.com/docs/guides/text and https://platform.openai.com/docs/guides/structured-outputs

## Final Check Before Sharing

Before using a project in an application, portfolio, or interview, make sure the artifact clearly states:

- the data are synthetic
- the work is for learning and skill development
- the result is not clinical, diagnostic, regulatory, or drug-efficacy evidence
- the interpretation includes at least one limitation
- the student can explain the code and figure in their own words
