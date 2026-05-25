import numpy as np

def flag_outliers_zscore(df, group_cols, value_col, threshold=1.5):
    result = df.copy()
    result["group_mean"] = result.groupby(group_cols)[value_col].transform("mean")
    result["group_sd"] = result.groupby(group_cols)[value_col].transform("std")
    result["z_score"] = (result[value_col] - result["group_mean"]) / result["group_sd"]
    result["qc_flag"] = np.where(result["z_score"].abs() > threshold, "review", "ok")
    return result
