"""Convenience paths for sample datasets."""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"

ENZYME_CLEAN = DATA_DIR / "enzyme_activity" / "enzyme_activity_clean.csv"
DRUG_RESPONSE_CLEAR = DATA_DIR / "drug_response" / "drug_response_clear.csv"
DRUG_RESPONSE_OUTLIER = DATA_DIR / "drug_response" / "drug_response_outlier.csv"
GENE_EXPRESSION_SMALL = DATA_DIR / "gene_expression" / "gene_expression_small_clean.csv"
