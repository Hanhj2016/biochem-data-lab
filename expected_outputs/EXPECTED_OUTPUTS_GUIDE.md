# Expected Outputs Guide

Use this guide to compare student interpretations with the intended learning points for scenario datasets. These notes are educational only and do not support clinical, diagnostic, regulatory, drug-efficacy, or real biological claims.


---

## Expected Learning Points: ai_figure_caption_review.csv

### Main Observation

Several synthetic AI-style captions sound confident but make claims beyond the dataset; the safer captions keep the observation and add boundaries.

### Data Quality Notes

The dataset teaches human-in-the-loop review and source-aware scientific writing rather than automatic acceptance of polished text.

### Suggested Next Step

Trace each caption back to the figure and dataset, then revise unsupported claims into cautious observations.

### Caution / Limitation

This rule-based review is a teaching tool, not a complete AI safety or scientific review system.

---

## Expected Learning Points: assay_development_day_variability.csv

### Main Observation

CompoundB has synthetic day-to-day shifts at higher concentrations, while most other matched summaries are closer across days.

### Data Quality Notes

The dataset teaches that an apparent response pattern should be checked for day or batch effects before stronger interpretation.

### Suggested Next Step

Review day-specific conditions such as timing, reagent lot, plate handling, and instrument settings in a real workflow.

### Caution / Limitation

The data are synthetic and should not be used as drug-efficacy or assay-validation evidence.

---

## Expected Learning Points: bioinformatics_sequence_triage.csv

### Main Observation

The synthetic sequences vary in GC content and motif count, and one sequence contains ambiguous bases that should be reviewed.

### Data Quality Notes

The dataset teaches that sequence summaries are useful first checks, but ambiguous bases and short length limit interpretation.

### Suggested Next Step

Review sequence quality or source notes before using ambiguous sequences in downstream analysis.

### Caution / Limitation

Short synthetic sequence summaries do not prove biological function.

---

## Expected Learning Points: drug_response_clear.csv

### Main Observation

Both synthetic compounds show lower mean cell viability at higher concentrations. CompoundA shows a stronger decrease than CompoundB in this teaching dataset.

### Data Quality Notes

The replicate values are consistent enough for a first dose-response visualization. This is a clean practice dataset for calculating mean, SD, SEM, and plotting grouped curves.

### Suggested Next Step

Add more concentrations near the middle of the response curve and compare the pattern with a noisier or outlier-containing dataset.

### Caution / Limitation

This is synthetic data for learning. Do not describe the result as clinical evidence, treatment evidence, or real drug efficacy.

---

## Expected Learning Points: drug_response_noisy.csv

### Main Observation

The overall pattern still suggests lower cell viability at higher concentrations, but the replicate values vary more than in the clean dataset.

### Data Quality Notes

Noisy replicates make the trend less visually confident. Students should notice wider spread within concentration groups and avoid relying on a single point.

### Suggested Next Step

Calculate mean, SD, SEM, and `n` for each compound and concentration. Then compare the plot with `drug_response_clear.csv` to see how variability changes interpretation.

### Caution / Limitation

Avoid strong claims from noisy synthetic data. In a real experiment, variability would need follow-up checks such as plate layout, pipetting notes, and replicate planning.

---

## Expected Learning Points: drug_response_outlier.csv

### Main Observation

Most replicate values follow a dose-response pattern, but a few individual points look inconsistent with nearby replicates at the same compound and concentration.

### Data Quality Notes

Potential outliers should be flagged for review, not automatically removed. A scatter plot of individual replicate points is more useful than a summary-only plot for this dataset.

### Suggested Next Step

Create a QC plot, calculate within-group z-scores, and compare mean versus median summaries while keeping the original data visible.

### Caution / Limitation

Outlier decisions need scientific justification. This synthetic dataset is for practicing review language, not for making drug-efficacy claims.

---

## Expected Learning Points: enzyme_activity_outlier.csv

### Main Observation

Most treatment samples have lower enzyme activity than the control samples, but one treatment replicate is unusually high compared with the rest of its group.

### Data Quality Notes

The unusual value can pull the treatment mean upward and make the group comparison less clear. A dot plot or box plot should be used alongside summary statistics.

### Suggested Next Step

Flag the unusual replicate for review, compare mean and median values, and write down what lab notes would need to be checked.

### Caution / Limitation

Do not remove a value only because it changes the result. This is synthetic learning data and does not prove an enzyme mechanism.

---

## Expected Learning Points: gene_expression_matrix_pca.csv

### Main Observation

The toy expression matrix is designed so control, low-treatment, and high-treatment samples can show visible pattern differences in a heatmap or PCA-style sample map.

### Data Quality Notes

The matrix has consistent sample columns and no missing values, making it suitable for practicing gene-wise z-scores, heatmaps, and PCA-style visualization.

### Suggested Next Step

Create a gene-wise z-score heatmap, then make a PCA-style sample map to compare whether samples from similar conditions cluster visually.

### Caution / Limitation

This is not a full RNA-seq workflow. Visual clustering does not prove biological mechanism, diagnostic meaning, or treatment effect.

---

## Expected Learning Points: gene_expression_small_clean.csv

### Main Observation

Some genes are higher in the treatment samples, some are lower, and housekeeping-like genes stay relatively stable in this toy dataset.

### Data Quality Notes

The replicate values are tidy and consistent enough for practicing mean expression, fold change, and log2 fold change.

### Suggested Next Step

Calculate log2 fold change for each gene and create a bar chart sorted from lower expression to higher expression.

### Caution / Limitation

Fold change alone does not prove biological function or diagnostic meaning. Real gene expression analysis needs normalization, quality control, statistical testing, and validation.

---

## Expected Learning Points: molecular_biology_qpcr_review.csv

### Main Observation

Most synthetic Ct replicate groups are tight, while treatment MYC has a larger replicate spread that should be reviewed.

### Data Quality Notes

The dataset teaches that relative-expression interpretation depends on replicate consistency and housekeeping/control checks.

### Suggested Next Step

Inspect the individual Ct values for the flagged gene and consider whether a replicate, primer, or plate-position issue should be reviewed.

### Caution / Limitation

The synthetic qPCR data are for learning and are not diagnostic or clinical evidence.

---

## Expected Learning Points: qc_plate_batch_review.csv

### Main Observation

Most control groups stay within the expected range, while the synthetic Batch_B sample group includes values that should be reviewed.

### Data Quality Notes

The dataset is designed to show that batch and plate-region context can matter. A group-level summary should be paired with review flags rather than treated as a final pass/fail decision.

### Suggested Next Step

Inspect the wells contributing to the review group and compare edge versus interior behavior before writing a final interpretation.

### Caution / Limitation

This is synthetic QC practice, not SOP-controlled release testing or regulatory evidence.

---

## Expected Learning Points: research_assistant_replicate_log.csv

### Main Observation

The synthetic inhibitor groups show lower activity than control, but one condition has a missing replicate and another has high variability.

### Data Quality Notes

The dataset teaches that group means are easier to interpret when replicate counts are balanced and variability is visible.

### Suggested Next Step

Check the bench note, repeat or recover the missing replicate if appropriate, and report uncertainty in the mini-summary.

### Caution / Limitation

The synthetic data can support practice in design review, but it cannot prove enzyme mechanism or inhibitor performance.
