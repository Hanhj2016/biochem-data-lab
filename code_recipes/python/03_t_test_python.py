from scipy import stats

def run_t_test(df, group_col, value_col, group_a, group_b):
    a = df[df[group_col] == group_a][value_col].dropna()
    b = df[df[group_col] == group_b][value_col].dropna()
    return stats.ttest_ind(a, b, equal_var=False)
