import pandas as pd
import pytest

from src.biochem_stats import (
    calculate_fold_change,
    run_anova,
    run_t_test,
    summary_mean_sd_sem,
)
from src.data_quality import flag_outliers_zscore, simple_data_quality_score
from src.enzyme_kinetics import fit_michaelis_menten, make_prediction_table, summarize_velocity
from src.growth_curve import estimate_log_phase_rate, summarize_growth
from src.plate_qc import add_plate_position_flags, make_plate_matrix, summarize_edge_effect
from src.qpcr import calculate_delta_delta_ct
from src.sequence_basics import count_motif, gc_content, reverse_complement, summarize_sequences
from src.sample_data import (
    BRADFORD_STANDARD_CURVE,
    DRUG_RESPONSE_OUTLIER,
    ENZYME_CLEAN,
    ENZYME_OUTLIER,
    ENZYME_THREE_GROUPS,
    GENE_EXPRESSION_SMALL,
    MICHAELIS_MENTEN_CLEAN,
)
from src.standard_curve import (
    estimate_unknown_concentrations,
    fit_linear_standard_curve,
    summarize_standard_curve,
    summarize_unknown_estimates,
)


def test_summary_mean_sd_sem_groups_enzyme_activity():
    df = pd.read_csv(ENZYME_CLEAN)

    summary = summary_mean_sd_sem(df, "group", "enzyme_activity")

    assert set(summary["group"]) == {"control", "treatment"}
    assert set(summary.columns) == {"group", "mean_value", "sd_value", "n", "sem_value"}
    assert summary["n"].tolist() == [6, 6]


def test_run_t_test_detects_group_difference():
    df = pd.read_csv(ENZYME_CLEAN)

    result = run_t_test(df, "group", "enzyme_activity", "control", "treatment")

    assert result.pvalue < 0.05


def test_run_anova_returns_group_row():
    df = pd.read_csv(ENZYME_THREE_GROUPS)

    table = run_anova(df, "group", "enzyme_activity")

    assert "C(group)" in table.index
    assert table.loc["C(group)", "PR(>F)"] < 0.05


def test_calculate_fold_change_adds_expected_columns():
    df = pd.read_csv(GENE_EXPRESSION_SMALL)

    result = calculate_fold_change(
        df,
        ["control_1", "control_2", "control_3"],
        ["treatment_1", "treatment_2", "treatment_3"],
    )

    assert {"control_mean", "treatment_mean", "fold_change", "log2_fold_change"}.issubset(result.columns)
    egfr = result[result["gene"] == "EGFR"].iloc[0]
    assert egfr["fold_change"] > 1


def test_flag_outliers_zscore_marks_review_points():
    df = pd.read_csv(DRUG_RESPONSE_OUTLIER)

    flagged = flag_outliers_zscore(df, ["drug_name", "concentration_uM"], "cell_viability_percent", threshold=1.0)

    assert "qc_flag" in flagged.columns
    assert "review" in set(flagged["qc_flag"])


def test_simple_data_quality_score_notes_missing_columns():
    df = pd.read_csv(ENZYME_OUTLIER)

    report = simple_data_quality_score(df, ["sample_id", "group", "enzyme_activity", "missing_column"])

    assert report["score"] < 100
    assert any("Missing columns" in note for note in report["notes"])


def test_helpers_raise_clear_error_for_missing_columns():
    df = pd.DataFrame({"group": ["control", "treatment"], "value": [1, 2]})

    with pytest.raises(ValueError, match="Missing required columns"):
        summary_mean_sd_sem(df, "group", "enzyme_activity")


def test_michaelis_menten_helpers_fit_clean_dataset():
    df = pd.read_csv(MICHAELIS_MENTEN_CLEAN)

    summary = summarize_velocity(df)
    params = fit_michaelis_menten(summary)
    curve = make_prediction_table(params, summary["substrate_mM"].min(), summary["substrate_mM"].max(), points=20)

    assert {"mean_velocity", "sd_velocity", "n", "sem_velocity"}.issubset(summary.columns)
    assert params["vmax"] > summary["mean_velocity"].max()
    assert params["km"] > 0
    assert len(curve) == 20
    assert curve["predicted_velocity"].is_monotonic_increasing


def test_standard_curve_helpers_estimate_unknowns():
    df = pd.read_csv(BRADFORD_STANDARD_CURVE)

    standard_summary = summarize_standard_curve(df)
    fit = fit_linear_standard_curve(df)
    estimates = estimate_unknown_concentrations(df, fit)
    unknown_summary = summarize_unknown_estimates(estimates)

    assert {"mean_absorbance", "sd_absorbance", "n", "sem_absorbance"}.issubset(standard_summary.columns)
    assert fit["slope"] > 0
    assert fit["r_squared"] > 0.99
    assert len(estimates) == 9
    assert set(unknown_summary["unknown_id"]) == {"UNK_A", "UNK_B", "UNK_C"}
    assert unknown_summary["any_outside_standard_range"].any()


def test_plate_qc_helpers_make_matrix():
    df = pd.read_csv("data/assay_qc/plate_layout_edge_effect.csv")

    flagged = add_plate_position_flags(df)
    matrix = make_plate_matrix(flagged)
    edge_summary = summarize_edge_effect(flagged)

    assert matrix.shape == (8, 12)
    assert flagged["is_edge_well"].any()
    assert not edge_summary.empty


def test_qpcr_delta_delta_ct_results():
    df = pd.read_csv("data/qpcr/qpcr_delta_ct_sample.csv")

    result = calculate_delta_delta_ct(df)
    treatment = result[result["condition"] == "treatment"]

    assert set(treatment["gene"]) == {"EGFR", "MYC", "TP53"}
    assert treatment.loc[treatment["gene"] == "EGFR", "relative_expression"].iloc[0] > 1


def test_growth_curve_rate_estimate():
    df = pd.read_csv("data/growth_curve/bacterial_growth_curve.csv")

    summary = summarize_growth(df)
    rates = estimate_log_phase_rate(summary)

    assert set(rates["strain"]) == {"StrainA", "StrainB"}
    assert (rates["doubling_time_hr"] > 0).all()


def test_sequence_basic_helpers():
    df = pd.read_csv("data/sequences/synthetic_sequences.csv")

    summary = summarize_sequences(df)

    assert gc_content("GCGC") == 100
    assert reverse_complement("ATGC") == "GCAT"
    assert count_motif("ATGATG", "ATG") == 2
    assert {"sequence_length", "gc_content_percent"}.issubset(summary.columns)
