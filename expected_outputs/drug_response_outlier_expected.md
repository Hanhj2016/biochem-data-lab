# Expected Learning Points: drug_response_outlier.csv

## Main Observation

Most replicate values follow a dose-response pattern, but a few individual points look inconsistent with nearby replicates at the same compound and concentration.

## Data Quality Notes

Potential outliers should be flagged for review, not automatically removed. A scatter plot of individual replicate points is more useful than a summary-only plot for this dataset.

## Suggested Next Step

Create a QC plot, calculate within-group z-scores, and compare mean versus median summaries while keeping the original data visible.

## Caution / Limitation

Outlier decisions need scientific justification. This synthetic dataset is for practicing review language, not for making drug-efficacy claims.
