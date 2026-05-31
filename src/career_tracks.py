"""Helpers for role-based synthetic career and academic advancement scenarios."""

from __future__ import annotations

import numpy as np
import pandas as pd

from src.ai_review import find_risky_terms, has_any_term, LIMITATION_TERMS
from src.sequence_basics import gc_content, count_motif


def _require_columns(df: pd.DataFrame, columns: list[str]) -> None:
    missing = [column for column in columns if column not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")


def summarize_qc_plate_batches(df: pd.DataFrame) -> pd.DataFrame:
    """Summarize synthetic plate batches and flag wells outside expected ranges."""
    _require_columns(
        df,
        [
            "batch_id",
            "plate_region",
            "sample_type",
            "cell_viability_percent",
            "expected_low",
            "expected_high",
        ],
    )
    result = df.copy()
    result["outside_expected_range"] = (
        (result["cell_viability_percent"] < result["expected_low"])
        | (result["cell_viability_percent"] > result["expected_high"])
    )
    summary = (
        result.groupby(["batch_id", "sample_type", "plate_region"])
        .agg(
            mean_viability=("cell_viability_percent", "mean"),
            sd_viability=("cell_viability_percent", "std"),
            n=("cell_viability_percent", "count"),
            review_wells=("outside_expected_range", "sum"),
        )
        .reset_index()
    )
    summary["sem_viability"] = summary["sd_viability"] / np.sqrt(summary["n"])
    summary["review_status"] = np.where(summary["review_wells"] > 0, "review", "ok")
    return summary


def summarize_replicate_design(df: pd.DataFrame) -> pd.DataFrame:
    """Summarize replicate balance and variability for a synthetic RA-style enzyme log."""
    _require_columns(df, ["condition", "planned_replicates", "enzyme_activity"])
    summary = (
        df.groupby("condition")
        .agg(
            mean_activity=("enzyme_activity", "mean"),
            sd_activity=("enzyme_activity", "std"),
            observed_replicates=("enzyme_activity", "count"),
            planned_replicates=("planned_replicates", "max"),
        )
        .reset_index()
    )
    summary["missing_replicates"] = summary["planned_replicates"] - summary["observed_replicates"]
    summary["sem_activity"] = summary["sd_activity"] / np.sqrt(summary["observed_replicates"])
    summary["review_status"] = "ok"
    summary.loc[summary["missing_replicates"] > 0, "review_status"] = "missing_replicate"
    summary.loc[(summary["review_status"] == "ok") & (summary["sd_activity"] > 6), "review_status"] = "high_variability"
    return summary


def summarize_assay_day_variability(df: pd.DataFrame) -> pd.DataFrame:
    """Compare synthetic dose-response summaries across assay days."""
    _require_columns(df, ["assay_day", "compound", "concentration_uM", "cell_viability_percent"])
    daily = (
        df.groupby(["compound", "concentration_uM", "assay_day"])
        .agg(
            mean_viability=("cell_viability_percent", "mean"),
            sd_viability=("cell_viability_percent", "std"),
            n=("cell_viability_percent", "count"),
        )
        .reset_index()
    )
    pivot = daily.pivot_table(
        index=["compound", "concentration_uM"], columns="assay_day", values="mean_viability"
    ).reset_index()
    if {"Day_1", "Day_2"}.issubset(pivot.columns):
        pivot["day_delta"] = pivot["Day_2"] - pivot["Day_1"]
        pivot["review_status"] = np.where(pivot["day_delta"].abs() > 8, "review_day_shift", "ok")
    else:
        pivot["day_delta"] = np.nan
        pivot["review_status"] = "single_day_only"
    return pivot


def summarize_qpcr_replicate_qc(df: pd.DataFrame) -> pd.DataFrame:
    """Summarize qPCR Ct replicate spread for synthetic molecular-biology lab data."""
    _require_columns(df, ["condition", "gene", "gene_type", "ct"])
    summary = (
        df.groupby(["condition", "gene", "gene_type"])
        .agg(mean_ct=("ct", "mean"), sd_ct=("ct", "std"), n=("ct", "count"))
        .reset_index()
    )
    summary["review_status"] = "ok"
    summary.loc[summary["n"] < 3, "review_status"] = "low_replicate_count"
    summary.loc[(summary["review_status"] == "ok") & (summary["sd_ct"] > 0.5), "review_status"] = "review_ct_spread"
    return summary


def summarize_sequence_triage(df: pd.DataFrame) -> pd.DataFrame:
    """Add beginner bioinformatics summary columns to synthetic sequence tasks."""
    _require_columns(df, ["sequence_id", "sequence", "motif_of_interest"])
    result = df.copy()
    result["sequence_length"] = result["sequence"].str.len()
    result["gc_content_percent"] = result["sequence"].map(gc_content)
    result["motif_count"] = result.apply(lambda row: count_motif(row["sequence"], row["motif_of_interest"]), axis=1)
    result["contains_ambiguous_base"] = result["sequence"].str.contains("N", case=False, regex=False)
    result["review_status"] = np.where(result["contains_ambiguous_base"], "review_ambiguous_base", "ok")
    return result


def review_ai_captions(df: pd.DataFrame) -> pd.DataFrame:
    """Flag AI-style figure captions that need human scientific review."""
    _require_columns(df, ["ai_caption"])
    result = df.copy()
    result["risky_claim_categories"] = result["ai_caption"].map(find_risky_terms)
    result["risk_count"] = result["risky_claim_categories"].map(len)
    result["mentions_limitation"] = result["ai_caption"].map(lambda text: has_any_term(text, LIMITATION_TERMS))
    result["review_status"] = "ok"
    result.loc[result["risk_count"] > 0, "review_status"] = "revise_claim"
    result.loc[(result["review_status"] == "ok") & ~result["mentions_limitation"], "review_status"] = "add_limitation"
    return result


def make_role_track_table() -> pd.DataFrame:
    """Return a compact map from role track to dataset and portfolio artifact."""
    return pd.DataFrame(
        [
            {
                "track": "QC analyst",
                "dataset": "data/career_scenarios/qc_plate_batch_review.csv",
                "job_or_academic_skill": "plate-batch review and control-range checks",
                "portfolio_artifact": "plate QC summary with review wells",
            },
            {
                "track": "Research assistant",
                "dataset": "data/career_scenarios/research_assistant_replicate_log.csv",
                "job_or_academic_skill": "replicate balance and design review",
                "portfolio_artifact": "replicate summary with missing-replicate note",
            },
            {
                "track": "Assay development",
                "dataset": "data/career_scenarios/assay_development_day_variability.csv",
                "job_or_academic_skill": "day-to-day robustness comparison",
                "portfolio_artifact": "day-shift table and dose-response figure",
            },
            {
                "track": "Molecular biology lab",
                "dataset": "data/career_scenarios/molecular_biology_qpcr_review.csv",
                "job_or_academic_skill": "qPCR replicate Ct review",
                "portfolio_artifact": "Ct spread table with cautious qPCR note",
            },
            {
                "track": "Bioinformatics assistant",
                "dataset": "data/career_scenarios/bioinformatics_sequence_triage.csv",
                "job_or_academic_skill": "sequence triage and motif summary",
                "portfolio_artifact": "sequence summary table",
            },
            {
                "track": "AI scientific communication",
                "dataset": "data/career_scenarios/ai_figure_caption_review.csv",
                "job_or_academic_skill": "AI caption claim review and safer rewriting",
                "portfolio_artifact": "caption review with safer revision",
            },
        ]
    )
