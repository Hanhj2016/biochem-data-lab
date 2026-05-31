"""Helpers for reviewing AI-written synthetic lab summaries.

These functions do not call an AI service. They help students practice
human-in-the-loop review of AI-style draft text using simple rule checks.
"""

from __future__ import annotations

import re

import pandas as pd

RISKY_PATTERNS = {
    "proof_or_causality": [r"\bproves?\b", r"\bcaused?\b", r"\bblocks? the enzyme mechanism\b"],
    "drug_or_efficacy": [r"\bbetter drug\b", r"\beffective\b", r"\bdrug efficacy\b", r"\bkills?\b"],
    "clinical_or_diagnostic": [r"\bclinical\b", r"\bdiagnos(?:e|is|tic)\b", r"\bpatient\b", r"\btreatment response\b"],
    "unsupported_data_action": [r"\bshould be removed\b", r"\bdelete\b", r"\bremove outliers\b"],
    "unsupported_function": [r"\bfunctional genomic region\b", r"\bproves? biological function\b"],
}

BOUNDARY_TERMS = ["synthetic", "learning", "not clinical", "not diagnostic", "not evidence"]
LIMITATION_TERMS = ["limitation", "review", "caution", "should be checked", "does not prove", "not prove"]


def _require_columns(df: pd.DataFrame, columns: list[str]) -> None:
    missing = [column for column in columns if column not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")


def find_risky_terms(text: str) -> list[str]:
    """Return risky claim categories found in a draft summary."""
    text = str(text).lower()
    found = []
    for category, patterns in RISKY_PATTERNS.items():
        if any(re.search(pattern, text) for pattern in patterns):
            found.append(category)
    return found


def has_any_term(text: str, terms: list[str]) -> bool:
    """Return whether any plain-language term appears in text."""
    text = str(text).lower()
    return any(term in text for term in terms)


def review_ai_summaries(df: pd.DataFrame, draft_col: str = "ai_draft_summary") -> pd.DataFrame:
    """Flag AI-style summaries that need human review.

    The checks are intentionally simple and transparent for students.
    They are review prompts, not a substitute for domain review.
    """
    _require_columns(df, [draft_col])
    result = df.copy()
    result["risky_claim_categories"] = result[draft_col].map(find_risky_terms)
    result["risk_count"] = result["risky_claim_categories"].map(len)
    result["mentions_boundary"] = result[draft_col].map(lambda text: has_any_term(text, BOUNDARY_TERMS))
    result["mentions_limitation"] = result[draft_col].map(lambda text: has_any_term(text, LIMITATION_TERMS))
    result["review_status"] = "ok"
    result.loc[result["risk_count"] > 0, "review_status"] = "revise_claim"
    result.loc[(result["review_status"] == "ok") & ~result["mentions_limitation"], "review_status"] = "add_limitation"
    return result


def make_review_summary(reviewed_df: pd.DataFrame) -> pd.DataFrame:
    """Summarize review status counts for plotting or reporting."""
    _require_columns(reviewed_df, ["review_status"])
    return reviewed_df.groupby("review_status").size().reset_index(name="case_count")
