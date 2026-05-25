run_anova <- function(df, group_col, value_col) {
  formula <- as.formula(paste(value_col, "~", group_col))
  model <- aov(formula, data = df)
  summary(model)
}
