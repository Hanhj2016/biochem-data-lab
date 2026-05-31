import pandas as pd

from src.sample_data import (
    AI_FIGURE_CAPTION_REVIEW,
    ASSAY_DEVELOPMENT_DAY_VARIABILITY,
    BIOINFORMATICS_SEQUENCE_TRIAGE,
    MOLECULAR_BIOLOGY_QPCR_REVIEW,
    QC_PLATE_BATCH_REVIEW,
    RESEARCH_ASSISTANT_REPLICATE_LOG,
)
from src.career_tracks import (
    make_role_track_table,
    review_ai_captions,
    summarize_assay_day_variability,
    summarize_qc_plate_batches,
    summarize_qpcr_replicate_qc,
    summarize_replicate_design,
    summarize_sequence_triage,
)


print("Role track table")
print(make_role_track_table())

qc = pd.read_csv(QC_PLATE_BATCH_REVIEW)
print()
print("QC plate batch summary")
print(summarize_qc_plate_batches(qc).head(10))

replicates = pd.read_csv(RESEARCH_ASSISTANT_REPLICATE_LOG)
print()
print("Research assistant replicate summary")
print(summarize_replicate_design(replicates))

assay_days = pd.read_csv(ASSAY_DEVELOPMENT_DAY_VARIABILITY)
print()
print("Assay day variability summary")
print(summarize_assay_day_variability(assay_days))

qpcr = pd.read_csv(MOLECULAR_BIOLOGY_QPCR_REVIEW)
print()
print("qPCR replicate QC summary")
print(summarize_qpcr_replicate_qc(qpcr))

seq = pd.read_csv(BIOINFORMATICS_SEQUENCE_TRIAGE)
print()
print("Sequence triage summary")
print(summarize_sequence_triage(seq)[["sequence_id", "sequence_length", "gc_content_percent", "motif_count", "review_status"]])

captions = pd.read_csv(AI_FIGURE_CAPTION_REVIEW)
print()
print("AI caption review summary")
print(review_ai_captions(captions)[["case_id", "issue_type", "review_status", "risky_claim_categories"]])
