library(tidyverse)

# Helpers for synthetic Michaelis-Menten-style enzyme kinetics examples.

require_columns <- function(df, columns) {
  missing <- setdiff(columns, names(df))
  if (length(missing) > 0) {
    stop(paste("Missing required columns:", paste(missing, collapse = ", ")))
  }
}

michaelis_menten <- function(substrate, vmax, km) {
  (vmax * substrate) / (km + substrate)
}

summarize_velocity <- function(df, substrate_col = "substrate_mM", velocity_col = "initial_velocity") {
  require_columns(df, c(substrate_col, velocity_col))
  df %>%
    group_by(.data[[substrate_col]]) %>%
    summarise(
      mean_velocity = mean(.data[[velocity_col]], na.rm = TRUE),
      sd_velocity = sd(.data[[velocity_col]], na.rm = TRUE),
      n = sum(!is.na(.data[[velocity_col]])),
      sem_velocity = sd_velocity / sqrt(n),
      .groups = "drop"
    )
}

fit_michaelis_menten <- function(summary_df, substrate_col = "substrate_mM", velocity_col = "mean_velocity") {
  require_columns(summary_df, c(substrate_col, velocity_col))
  if (nrow(summary_df) < 3) {
    stop("At least three substrate concentrations are needed for this educational fit.")
  }
  fit <- nls(
    as.formula(paste(velocity_col, "~ (vmax *", substrate_col, ") / (km +", substrate_col, ")")),
    data = summary_df,
    start = list(vmax = max(summary_df[[velocity_col]], na.rm = TRUE), km = median(summary_df[[substrate_col]], na.rm = TRUE)),
    algorithm = "port",
    lower = c(vmax = 0, km = 0)
  )
  params <- coef(fit)
  list(vmax = unname(params[["vmax"]]), km = unname(params[["km"]]), fit = fit)
}

make_prediction_table <- function(params, min_substrate, max_substrate, points = 100) {
  tibble(substrate_mM = seq(min_substrate, max_substrate, length.out = points)) %>%
    mutate(predicted_velocity = michaelis_menten(substrate_mM, params$vmax, params$km))
}
