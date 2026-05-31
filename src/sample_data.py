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

# Legacy foundation/sample datasets used by early notebooks.
ENZYME_ACTIVITY_SAMPLE = DATA_DIR / "enzyme_activity_sample.csv"
ANOVA_CELL_VIABILITY_SAMPLE = DATA_DIR / "anova_cell_viability_sample.csv"
CELL_VIABILITY_SAMPLE = DATA_DIR / "cell_viability_sample.csv"
DOSE_RESPONSE_IC50_SAMPLE = DATA_DIR / "dose_response_ic50_sample.csv"
QC_OUTLIER_SAMPLE = DATA_DIR / "qc_outlier_sample.csv"
GENE_EXPRESSION_TOY = DATA_DIR / "gene_expression_toy.csv"
GENE_EXPRESSION_MATRIX_TOY = DATA_DIR / "gene_expression_matrix_toy.csv"

PLATE_LAYOUT_EDGE_EFFECT = DATA_DIR / "assay_qc" / "plate_layout_edge_effect.csv"
QPCR_DELTA_CT_SAMPLE = DATA_DIR / "qpcr" / "qpcr_delta_ct_sample.csv"
BACTERIAL_GROWTH_CURVE = DATA_DIR / "growth_curve" / "bacterial_growth_curve.csv"
SYNTHETIC_SEQUENCES = DATA_DIR / "sequences" / "synthetic_sequences.csv"
AI_LITERACY_SUMMARY_REVIEW_CASES = DATA_DIR / "ai_literacy" / "ai_lab_summary_review_cases.csv"


CAREER_SCENARIOS_DIR = DATA_DIR / "career_scenarios"
QC_PLATE_BATCH_REVIEW = CAREER_SCENARIOS_DIR / "qc_plate_batch_review.csv"
RESEARCH_ASSISTANT_REPLICATE_LOG = CAREER_SCENARIOS_DIR / "research_assistant_replicate_log.csv"
ASSAY_DEVELOPMENT_DAY_VARIABILITY = CAREER_SCENARIOS_DIR / "assay_development_day_variability.csv"
MOLECULAR_BIOLOGY_QPCR_REVIEW = CAREER_SCENARIOS_DIR / "molecular_biology_qpcr_review.csv"
BIOINFORMATICS_SEQUENCE_TRIAGE = CAREER_SCENARIOS_DIR / "bioinformatics_sequence_triage.csv"
AI_FIGURE_CAPTION_REVIEW = CAREER_SCENARIOS_DIR / "ai_figure_caption_review.csv"
