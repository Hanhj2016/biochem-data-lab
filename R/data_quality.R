library(tidyverse)

missing_value_report <- function(df) {
  tibble(
    column = names(df),
    missing_count = sapply(df, function(x) sum(is.na(x))),
    missing_percent = round(sapply(df, function(x) mean(is.na(x)) * 100), 2)
  )
}

flag_outliers_zscore <- function(df, group_cols, value_col, threshold = 1.5) {
  df %>%
    group_by(across(all_of(group_cols))) %>%
    mutate(
      group_mean = mean(.data[[value_col]], na.rm = TRUE),
      group_sd = sd(.data[[value_col]], na.rm = TRUE),
      z_score = (.data[[value_col]] - group_mean) / group_sd,
      qc_flag = if_else(abs(z_score) > threshold, "review", "ok")
    ) %>%
    ungroup()
}
