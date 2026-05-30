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


def test_role_track_table_lists_six_tracks():
    table = make_role_track_table()

    assert len(table) == 6
    assert {"track", "dataset", "job_or_academic_skill", "portfolio_artifact"}.issubset(table.columns)


def test_career_qc_plate_summary_flags_review_batch():
    df = pd.read_csv("data/career_scenarios/qc_plate_batch_review.csv")

    summary = summarize_qc_plate_batches(df)

    assert "review_status" in summary.columns
    assert "review" in set(summary["review_status"])


def test_replicate_design_flags_missing_and_high_variability():
    df = pd.read_csv("data/career_scenarios/research_assistant_replicate_log.csv")

    summary = summarize_replicate_design(df)

    assert "missing_replicate" in set(summary["review_status"])
    assert "high_variability" in set(summary["review_status"])


def test_assay_day_variability_flags_day_shift():
    df = pd.read_csv("data/career_scenarios/assay_development_day_variability.csv")

    summary = summarize_assay_day_variability(df)

    assert "review_day_shift" in set(summary["review_status"])


def test_qpcr_review_flags_ct_spread():
    df = pd.read_csv("data/career_scenarios/molecular_biology_qpcr_review.csv")

    summary = summarize_qpcr_replicate_qc(df)

    assert "review_ct_spread" in set(summary["review_status"])


def test_sequence_triage_flags_ambiguous_base():
    df = pd.read_csv("data/career_scenarios/bioinformatics_sequence_triage.csv")

    summary = summarize_sequence_triage(df)

    assert "review_ambiguous_base" in set(summary["review_status"])
    assert "gc_content_percent" in summary.columns


def test_ai_caption_review_flags_risky_claims():
    df = pd.read_csv("data/career_scenarios/ai_figure_caption_review.csv")

    reviewed = review_ai_captions(df)

    assert "revise_claim" in set(reviewed["review_status"])
    assert reviewed["risk_count"].max() > 0
