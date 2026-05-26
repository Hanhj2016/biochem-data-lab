# Drug Response QC / Outlier Challenge

## Mission

Check whether a synthetic assay dataset has suspicious replicate values that should be reviewed before interpretation.

## Dataset Path

```text
data/drug_response/drug_response_outlier.csv
```

## Tasks

1. Plot all replicate points by concentration and compound.
2. Calculate summary statistics for each compound and concentration.
3. Flag suspicious values using a simple within-group z-score or visual rule.
4. Compare the summary with and without flagged points, but do not automatically delete them.
5. Write what should be checked in a lab record before deciding what to do.

## Bonus Task

Create a simple data quality score with notes explaining why the dataset needs review.

## Expected Visual Output

A QC scatter plot showing individual replicate points, with flagged values highlighted by color or symbol.
