from pathlib import Path

import pandas as pd

from src.career_tracks import (
    make_role_track_table,
    review_ai_captions,
    summarize_assay_day_variability,
    summarize_qc_plate_batches,
    summarize_qpcr_replicate_qc,
    summarize_replicate_design,
    summarize_sequence_triage,
)

DATA_DIR = Path("data") / "career_scenarios"

print("Role track table")
print(make_role_track_table())

qc = pd.read_csv(DATA_DIR / "qc_plate_batch_review.csv")
print()
print("QC plate batch summary")
print(summarize_qc_plate_batches(qc).head(10))

replicates = pd.read_csv(DATA_DIR / "research_assistant_replicate_log.csv")
print()
print("Research assistant replicate summary")
print(summarize_replicate_design(replicates))

assay_days = pd.read_csv(DATA_DIR / "assay_development_day_variability.csv")
print()
print("Assay day variability summary")
print(summarize_assay_day_variability(assay_days))

qpcr = pd.read_csv(DATA_DIR / "molecular_biology_qpcr_review.csv")
print()
print("qPCR replicate QC summary")
print(summarize_qpcr_replicate_qc(qpcr))

seq = pd.read_csv(DATA_DIR / "bioinformatics_sequence_triage.csv")
print()
print("Sequence triage summary")
print(summarize_sequence_triage(seq)[["sequence_id", "sequence_length", "gc_content_percent", "motif_count", "review_status"]])

captions = pd.read_csv(DATA_DIR / "ai_figure_caption_review.csv")
print()
print("AI caption review summary")
print(review_ai_captions(captions)[["case_id", "issue_type", "review_status", "risky_claim_categories"]])
