library(tidyverse)

summary_mean_sd_sem <- function(df, group_col, value_col) {
  df %>%
    group_by(.data[[group_col]]) %>%
    summarise(
      mean_value = mean(.data[[value_col]], na.rm = TRUE),
      sd_value = sd(.data[[value_col]], na.rm = TRUE),
      n = sum(!is.na(.data[[value_col]])),
      sem_value = sd_value / sqrt(n),
      .groups = "drop"
    )
}

run_t_test <- function(df, group_col, value_col) {
  formula <- as.formula(paste(value_col, "~", group_col))
  t.test(formula, data = df)
}

run_anova <- function(df, group_col, value_col) {
  formula <- as.formula(paste(value_col, "~", group_col))
  model <- aov(formula, data = df)
  summary(model)
}

calculate_fold_change <- function(df, control_cols, treatment_cols) {
  df %>%
    rowwise() %>%
    mutate(
      control_mean = mean(c_across(all_of(control_cols)), na.rm = TRUE),
      treatment_mean = mean(c_across(all_of(treatment_cols)), na.rm = TRUE),
      fold_change = treatment_mean / control_mean,
      log2_fold_change = log2(fold_change)
    ) %>%
    ungroup()
}
