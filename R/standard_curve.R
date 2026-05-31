library(tidyverse)

# Helpers for synthetic Bradford-style standard curve examples.

require_columns <- function(df, columns) {
  missing <- setdiff(columns, names(df))
  if (length(missing) > 0) {
    stop(paste("Missing required columns:", paste(missing, collapse = ", ")))
  }
}

summarize_standard_curve <- function(df) {
  require_columns(df, c("sample_type", "known_concentration_mg_ml", "absorbance_595"))
  df %>%
    filter(sample_type == "standard", !is.na(known_concentration_mg_ml)) %>%
    group_by(known_concentration_mg_ml) %>%
    summarise(
      mean_absorbance = mean(absorbance_595, na.rm = TRUE),
      sd_absorbance = sd(absorbance_595, na.rm = TRUE),
      n = sum(!is.na(absorbance_595)),
      sem_absorbance = sd_absorbance / sqrt(n),
      .groups = "drop"
    )
}

fit_linear_standard_curve <- function(df) {
  require_columns(df, c("sample_type", "known_concentration_mg_ml", "absorbance_595"))
  standards <- df %>% filter(sample_type == "standard", !is.na(known_concentration_mg_ml), !is.na(absorbance_595))
  model <- lm(absorbance_595 ~ known_concentration_mg_ml, data = standards)
  list(
    model = model,
    slope = unname(coef(model)[["known_concentration_mg_ml"]]),
    intercept = unname(coef(model)[["(Intercept)"]]),
    r_squared = summary(model)$r.squared,
    min_standard = min(standards$known_concentration_mg_ml),
    max_standard = max(standards$known_concentration_mg_ml)
  )
}

estimate_unknown_concentrations <- function(df, fit) {
  require_columns(df, c("sample_id", "sample_type", "absorbance_595"))
  df %>%
    filter(sample_type == "unknown") %>%
    mutate(
      estimated_concentration_mg_ml = (absorbance_595 - fit$intercept) / fit$slope,
      outside_standard_range = estimated_concentration_mg_ml < fit$min_standard | estimated_concentration_mg_ml > fit$max_standard
    )
}

summarize_unknown_estimates <- function(estimates) {
  require_columns(estimates, c("sample_id", "estimated_concentration_mg_ml", "outside_standard_range"))
  estimates %>%
    mutate(unknown_id = str_extract(sample_id, "UNK_[A-Za-z0-9]+")) %>%
    group_by(unknown_id) %>%
    summarise(
      mean_estimated_concentration = mean(estimated_concentration_mg_ml, na.rm = TRUE),
      sd_estimated_concentration = sd(estimated_concentration_mg_ml, na.rm = TRUE),
      n = sum(!is.na(estimated_concentration_mg_ml)),
      sem_estimated_concentration = sd_estimated_concentration / sqrt(n),
      any_outside_standard_range = any(outside_standard_range),
      .groups = "drop"
    )
}
