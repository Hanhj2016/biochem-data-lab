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


def test_role_track_table_lists_six_tracks():
    table = make_role_track_table()

    assert len(table) == 6
    assert {"track", "dataset", "job_or_academic_skill", "portfolio_artifact"}.issubset(table.columns)


def test_career_qc_plate_summary_flags_review_batch():
    df = pd.read_csv(QC_PLATE_BATCH_REVIEW)

    summary = summarize_qc_plate_batches(df)

    assert "review_status" in summary.columns
    assert "review" in set(summary["review_status"])


def test_replicate_design_flags_missing_and_high_variability():
    df = pd.read_csv(RESEARCH_ASSISTANT_REPLICATE_LOG)

    summary = summarize_replicate_design(df)

    assert "missing_replicate" in set(summary["review_status"])
    assert "high_variability" in set(summary["review_status"])


def test_assay_day_variability_flags_day_shift():
    df = pd.read_csv(ASSAY_DEVELOPMENT_DAY_VARIABILITY)

    summary = summarize_assay_day_variability(df)

    assert "review_day_shift" in set(summary["review_status"])


def test_qpcr_review_flags_ct_spread():
    df = pd.read_csv(MOLECULAR_BIOLOGY_QPCR_REVIEW)

    summary = summarize_qpcr_replicate_qc(df)

    assert "review_ct_spread" in set(summary["review_status"])


def test_sequence_triage_flags_ambiguous_base():
    df = pd.read_csv(BIOINFORMATICS_SEQUENCE_TRIAGE)

    summary = summarize_sequence_triage(df)

    assert "review_ambiguous_base" in set(summary["review_status"])
    assert "gc_content_percent" in summary.columns


def test_ai_caption_review_flags_risky_claims():
    df = pd.read_csv(AI_FIGURE_CAPTION_REVIEW)

    reviewed = review_ai_captions(df)

    assert "revise_claim" in set(reviewed["review_status"])
    assert reviewed["risk_count"].max() > 0
