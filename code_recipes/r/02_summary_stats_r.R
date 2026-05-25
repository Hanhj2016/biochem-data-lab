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
