library(tidyverse)

# Helpers for synthetic OD600 growth curve examples.

require_columns <- function(df, columns) {
  missing <- setdiff(columns, names(df))
  if (length(missing) > 0) {
    stop(paste("Missing required columns:", paste(missing, collapse = ", ")))
  }
}

summarize_growth <- function(df) {
  require_columns(df, c("strain", "time_hr", "od600"))
  df %>%
    group_by(strain, time_hr) %>%
    summarise(
      mean_od600 = mean(od600, na.rm = TRUE),
      sd_od600 = sd(od600, na.rm = TRUE),
      n = sum(!is.na(od600)),
      sem_od600 = sd_od600 / sqrt(n),
      .groups = "drop"
    )
}

estimate_log_phase_rate <- function(summary_df, start_hr = 2, end_hr = 6) {
  require_columns(summary_df, c("strain", "time_hr", "mean_od600"))
  summary_df %>%
    filter(time_hr >= start_hr, time_hr <= end_hr, mean_od600 > 0) %>%
    group_by(strain) %>%
    summarise(
      log_phase_rate_per_hr = coef(lm(log(mean_od600) ~ time_hr))[2],
      doubling_time_hr = log(2) / log_phase_rate_per_hr,
      .groups = "drop"
    )
}
