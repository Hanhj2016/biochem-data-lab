library(tidyverse)

# Helpers for synthetic qPCR delta-delta Ct examples.

require_columns <- function(df, columns) {
  missing <- setdiff(columns, names(df))
  if (length(missing) > 0) {
    stop(paste("Missing required columns:", paste(missing, collapse = ", ")))
  }
}

mean_ct_by_group <- function(df, ct_col = "ct_value") {
  require_columns(df, c("condition", "gene", ct_col))
  df %>%
    group_by(condition, gene) %>%
    summarise(
      mean_ct = mean(.data[[ct_col]], na.rm = TRUE),
      sd_ct = sd(.data[[ct_col]], na.rm = TRUE),
      n = sum(!is.na(.data[[ct_col]])),
      .groups = "drop"
    )
}

calculate_delta_delta_ct <- function(df, housekeeping_gene = "GAPDH", control_condition = "control", ct_col = "ct_value") {
  summary <- mean_ct_by_group(df, ct_col = ct_col)
  hk <- summary %>%
    filter(gene == housekeeping_gene) %>%
    select(condition, housekeeping_ct = mean_ct)
  merged <- summary %>%
    left_join(hk, by = "condition") %>%
    mutate(delta_ct = mean_ct - housekeeping_ct)
  control_delta <- merged %>%
    filter(condition == control_condition) %>%
    select(gene, control_delta_ct = delta_ct)
  merged %>%
    left_join(control_delta, by = "gene") %>%
    mutate(
      delta_delta_ct = delta_ct - control_delta_ct,
      relative_expression = 2^(-delta_delta_ct)
    ) %>%
    filter(gene != housekeeping_gene)
}
