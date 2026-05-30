# BioChem Data Lab: Student Project Menu

Choose one mini-project based on your interest and current comfort level. Each project uses synthetic data only and is meant for learning, not clinical, diagnostic, regulatory, or drug-efficacy claims.

## Beginner Projects

| Project | Goal | Dataset | Notebook | Visual Output | Time | Skill Practiced |
|---|---|---|---|---|---|---|
| Enzyme Activity Mini Report | Compare control and treatment enzyme activity. | `data/enzyme_activity/enzyme_activity_clean.csv` | `notebooks/01_Enzyme_Activity_Python.ipynb` | Bar chart with error bars | 45-60 min | Summary statistics and cautious interpretation |
| Control vs Treatment t-test | Practice a two-group statistical comparison. | `data/enzyme_activity_sample.csv` | `notebooks/02_T_Test_Python.ipynb` | Result table or short paragraph | 45-60 min | p-values, limitations, and scientific wording |
| Gene Expression Fold Change | Compare toy gene expression between control and treatment samples. | `data/gene_expression/gene_expression_small_clean.csv` | `notebooks/05_Gene_Expression_Python.ipynb` | Sorted fold-change bar chart | 60 min | Fold change and log2 fold change |

## Intermediate Projects

| Project | Goal | Dataset | Notebook | Visual Output | Time | Skill Practiced |
|---|---|---|---|---|---|---|
| Drug Response Screening Challenge | Compare synthetic compound responses across concentrations. | `data/drug_response/drug_response_clear.csv` | `notebooks/04_Dose_Response_Python.ipynb` | Dose-response curve | 60-90 min | Grouped summaries and concentration-response plots |
| QC Detective | Find suspicious assay values before interpretation. | `data/drug_response/drug_response_outlier.csv` | `notebooks/08_Advanced_Data_QC_Outlier_Visualization_Python.ipynb` | QC scatter plot | 60-90 min | Outlier review and data quality notes |
| Gene Expression Heatmap Explorer | Visualize toy expression patterns across samples. | `data/gene_expression/gene_expression_matrix_pca.csv` | `notebooks/09_Advanced_PCA_Heatmap_Gene_Expression_Python.ipynb` | Heatmap | 75-90 min | Z-scores and visual pattern recognition |
| PCA Sample Map Explorer | Compare sample patterns in a toy expression matrix. | `data/gene_expression/gene_expression_matrix_pca.csv` | `notebooks/09_Advanced_PCA_Heatmap_Gene_Expression_Python.ipynb` | PCA-style scatter plot | 75-90 min | Dimension reduction intuition |

## Challenge Prompts

These optional prompts are short project briefs that pair with the scenario datasets.

| Challenge | Topic | Prompt | Expected Visual Output | Difficulty |
|---|---|---|---|---|
| Drug Response Clear | concentration-response visualization | `challenge_prompts/Drug_Response_Clear_Challenge.md` | dose-response curve | Easy / Medium |
| Drug Response Noisy | variability and cautious interpretation | `challenge_prompts/Drug_Response_Noisy_Challenge.md` | points plus mean trend | Medium |
| QC Detective | outlier review | `challenge_prompts/Drug_Response_QC_Outlier_Challenge.md` | QC scatter plot | Easy / Medium |
| Enzyme Activity Outlier | replicate review | `challenge_prompts/Enzyme_Activity_Outlier_Challenge.md` | grouped dot plot or box plot | Easy / Medium |
| Gene Expression Small Clean | fold-change practice | `challenge_prompts/Gene_Expression_Small_Clean_Challenge.md` | sorted log2 fold-change chart | Easy |
| Gene Expression Heatmap | expression matrix patterns | `challenge_prompts/Gene_Expression_Heatmap_Challenge.md` | heatmap and optional PCA map | Medium |
| Literature Abstract Journal Club | scientific reading | `challenge_prompts/Literature_Abstract_Challenge.md` | discussion notes | Easy |
| QC Plate Batch Review | QC analyst role scenario | `challenge_prompts/QC_Plate_Batch_Review_Challenge.md` | batch summary or plate QC chart | Medium |
| Research Assistant Replicate Log | replicate and design review | `challenge_prompts/Research_Assistant_Replicate_Log_Challenge.md` | replicate-aware bar or dot plot | Medium |
| Assay Development Day Variability | day-to-day robustness | `challenge_prompts/Assay_Development_Day_Variability_Challenge.md` | dose-response by assay day | Medium |
| Molecular Biology qPCR Review | Ct replicate QC | `challenge_prompts/Molecular_Biology_qPCR_Review_Challenge.md` | Ct spread bar chart | Medium |
| Bioinformatics Sequence Triage | sequence summary and review | `challenge_prompts/Bioinformatics_Sequence_Triage_Challenge.md` | GC-content bar chart | Easy / Medium |
| AI Figure Caption Review | AI scientific communication | `challenge_prompts/AI_Figure_Caption_Review_Challenge.md` | review-status bar chart | Easy / Medium |

Suggested first challenge:

```text
QC Detective
```

Why:

```text
visual
practical
not too complex
useful for lab data thinking
```

## Advanced Challenge Projects

These projects are advanced or applied extensions. Some reuse earlier concepts, but each adds a new lab-data skill such as model fitting, calibration, plate-layout QC, qPCR normalization, time-course analysis, or sequence analysis. Python notebooks are primary for this section unless an R notebook is explicitly listed.

| Project | Goal | Dataset | Notebook | Visual Output | Time | Skill Practiced |
|---|---|---|---|---|---|---|
| Graphical Showcase Tour | See a visual overview of many BioChem Data Lab topics. | multiple synthetic datasets | `notebooks/11_Graphical_Showcase_Python.ipynb` | 10 interactive figures | 45-60 min | Scientific visualization selection |
| IC50-style Curve Fitting | Fit a simple educational dose-response curve. | `data/drug_response/drug_response_ic50_like.csv` | `notebooks/07_Advanced_IC50_Curve_Fitting_Python.ipynb` | Fitted curve | 90-120 min | Model fitting and parameter caution |
| Enzyme Kinetics Curve Fitting | Explore substrate concentration and initial velocity. | `data/enzyme_kinetics/michaelis_menten_clean.csv` | `notebooks/15_Enzyme_Kinetics_Michaelis_Menten_Python.ipynb` | Michaelis-Menten-style curve | 90-120 min | Saturation curves and parameter caution |
| Bradford Standard Curve | Estimate synthetic unknown protein concentrations from a calibration curve. | `data/standard_curves/bradford_standard_curve.csv` | `notebooks/16_Standard_Curve_Bradford_Assay_Python.ipynb` | Standard curve with unknown estimates | 75-90 min | Calibration, interpolation, and extrapolation caution |
| Plate QC Explorer | Inspect a 96-well-style plate for edge effects. | `data/assay_qc/plate_layout_edge_effect.csv` | `notebooks/17_Assay_QC_Plate_Layout_Python.ipynb` | Plate heatmap | 75-90 min | Spatial QC and control review |
| qPCR Delta-Delta Ct | Normalize synthetic Ct values to a housekeeping gene. | `data/qpcr/qpcr_delta_ct_sample.csv` | `notebooks/18_qPCR_Delta_Delta_Ct_Python.ipynb` | Relative expression bar chart | 75-90 min | Housekeeping normalization |
| Growth Curve Explorer | Compare synthetic OD600 growth patterns over time. | `data/growth_curve/bacterial_growth_curve.csv` | `notebooks/19_Growth_Curve_OD600_Python.ipynb` | Growth curve line plot | 75-90 min | Time-course summaries and growth-rate intuition |
| Sequence Basics Explorer | Summarize short synthetic DNA sequences. | `data/sequences/synthetic_sequences.csv` | `notebooks/20_Sequence_Basics_GC_Content_Python.ipynb` | GC-content bar chart | 60-75 min | Intro sequence analysis |
| Experimental Design Reviewer | Explain how replicates, controls, and variability affect interpretation. | `data/enzyme_activity/enzyme_activity_three_groups.csv` | `notebooks/14_Experimental_Design_and_Replicates_Python.ipynb` | Replicate plot and group summary | 90 min | Experimental design thinking |
| BioDose AI Bridge | Prepare reusable notebook logic for a future app. | `data/drug_response/drug_response_clear.csv`, `data/drug_response/drug_response_outlier.csv` | `notebooks/13_BioDose_AI_Bridge_Python.ipynb` | Dose-response chart and ranking table | 90-120 min | Workflow design and quality scoring |
| AI/LLM Lab Summary Reviewer | Review synthetic AI-style lab summaries for unsupported claims and safer wording. | `data/ai_literacy/ai_lab_summary_review_cases.csv` | `notebooks/21_AI_LLM_Lab_Summary_Review_Python.ipynb` | Review-status bar chart | 60-75 min | AI literacy, claim boundaries, and scientific communication |
| Career and Academic Advancement Tracks | Practice role-based lab, industry, and academic application scenarios. | `data/career_scenarios/` | `notebooks/22_Career_Academic_Advancement_Tracks_Python.ipynb` | QC summaries, replicate plots, sequence and caption review tables | 90-120 min | Portfolio and interview-ready scientific judgment |
| Literature Abstract Journal Club | Turn a fictional abstract into a structured academic summary. | `data/literature_abstracts/abstract_egfr_fictional.txt` | Challenge prompt | Discussion notes | 45-60 min | Reading, summarizing, and limitation spotting |

## Academic Application Extension

For master's applications, medical-school preparation, special research programs, internships, or research assistant applications, choose one project and turn it into an application-ready artifact using:

```text
ADVANCEMENT_AND_PORTFOLIO_GUIDE.md
writing_templates/academic_project_summary_template.md
writing_templates/application_reflection_template.md
writing_templates/academic_interview_prep_template.md
```

Suggested deliverable:

```text
one figure + one cautious result paragraph + one limitation + one next-step idea + one short reflection
```

Strong project choices for this purpose:

- `10_Capstone_BioDose_Advanced_Challenge.ipynb`
- `14_Experimental_Design_and_Replicates_Python.ipynb`
- `15_Enzyme_Kinetics_Michaelis_Menten_Python.ipynb`
- `16_Standard_Curve_Bradford_Assay_Python.ipynb`
- `18_qPCR_Delta_Delta_Ct_Python.ipynb`
- `21_AI_LLM_Lab_Summary_Review_Python.ipynb`
- `22_Career_Academic_Advancement_Tracks_Python.ipynb`

## Optional Extensions

- Add a figure caption using `writing_templates/figure_caption_template.md`.
- Add a results paragraph using `writing_templates/results_paragraph_template.md`.
- Add a limitations paragraph using `writing_templates/limitations_template.md`.
- Compare a clean dataset with a noisy or outlier dataset.
- Write one next-experiment idea using `writing_templates/next_experiment_template.md`.

## Project Checklist

Before calling a project finished, check:

1. Did you state the Biochemistry question?
2. Did you preview the dataset?
3. Did you make a visual output?
4. Did you write a cautious interpretation?
5. Did you include at least one limitation?
6. Did you avoid clinical, medical, diagnostic, regulatory, or drug-efficacy claims?
