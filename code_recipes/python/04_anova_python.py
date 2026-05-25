import statsmodels.api as sm
from statsmodels.formula.api import ols

def run_anova(df, group_col, value_col):
    model = ols(f"{value_col} ~ C({group_col})", data=df).fit()
    return sm.stats.anova_lm(model, typ=2)
