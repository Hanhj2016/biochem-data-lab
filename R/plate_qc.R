library(tidyverse)

# Helpers for synthetic plate-layout QC examples.

require_columns <- function(df, columns) {
  missing <- setdiff(columns, names(df))
  if (length(missing) > 0) {
    stop(paste("Missing required columns:", paste(missing, collapse = ", ")))
  }
}

add_plate_position_flags <- function(df) {
  require_columns(df, c("row", "column"))
  df %>% mutate(is_edge_well = row %in% c("A", "H") | column %in% c(1, 12))
}

summarize_edge_effect <- function(df, value_col = "cell_viability_percent") {
  require_columns(df, c("sample_type", "is_edge_well", value_col))
  df %>%
    group_by(sample_type, is_edge_well) %>%
    summarise(
      mean_value = mean(.data[[value_col]], na.rm = TRUE),
      sd_value = sd(.data[[value_col]], na.rm = TRUE),
      n = sum(!is.na(.data[[value_col]])),
      .groups = "drop"
    )
}
