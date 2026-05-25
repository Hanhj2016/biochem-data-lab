run_t_test <- function(df, group_col, value_col) {
  formula <- as.formula(paste(value_col, "~", group_col))
  t.test(formula, data = df)
}
