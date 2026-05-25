import numpy as np

def calculate_fold_change(df, control_cols, treatment_cols):
    result = df.copy()
    result["control_mean"] = result[control_cols].mean(axis=1)
    result["treatment_mean"] = result[treatment_cols].mean(axis=1)
    result["fold_change"] = result["treatment_mean"] / result["control_mean"]
    result["log2_fold_change"] = np.log2(result["fold_change"])
    return result
