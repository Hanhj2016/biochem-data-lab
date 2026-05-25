library(tidyverse)

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
