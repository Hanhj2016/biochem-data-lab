"""Convenience paths for synthetic sample datasets.

Example:
    df = pd.read_csv(ENZYME_CLEAN)
"""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"

ENZYME_CLEAN = DATA_DIR / "enzyme_activity" / "enzyme_activity_clean.csv"
ENZYME_OUTLIER = DATA_DIR / "enzyme_activity" / "enzyme_activity_outlier.csv"
ENZYME_THREE_GROUPS = DATA_DIR / "enzyme_activity" / "enzyme_activity_three_groups.csv"
DRUG_RESPONSE_CLEAR = DATA_DIR / "drug_response" / "drug_response_clear.csv"
DRUG_RESPONSE_NOISY = DATA_DIR / "drug_response" / "drug_response_noisy.csv"
DRUG_RESPONSE_OUTLIER = DATA_DIR / "drug_response" / "drug_response_outlier.csv"
GENE_EXPRESSION_SMALL = DATA_DIR / "gene_expression" / "gene_expression_small_clean.csv"
GENE_EXPRESSION_MATRIX_PCA = DATA_DIR / "gene_expression" / "gene_expression_matrix_pca.csv"
MICHAELIS_MENTEN_CLEAN = DATA_DIR / "enzyme_kinetics" / "michaelis_menten_clean.csv"
MICHAELIS_MENTEN_NOISY = DATA_DIR / "enzyme_kinetics" / "michaelis_menten_noisy.csv"
BRADFORD_STANDARD_CURVE = DATA_DIR / "standard_curves" / "bradford_standard_curve.csv"
