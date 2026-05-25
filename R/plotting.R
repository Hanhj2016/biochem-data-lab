library(tidyverse)

plot_group_means <- function(summary_df, group_col, mean_col, sem_col, title) {
  ggplot(summary_df, aes(x = .data[[group_col]], y = .data[[mean_col]])) +
    geom_col() +
    geom_errorbar(aes(
      ymin = .data[[mean_col]] - .data[[sem_col]],
      ymax = .data[[mean_col]] + .data[[sem_col]]
    ), width = 0.2) +
    labs(title = title)
}

plot_dose_response <- function(summary_df) {
  summary_df %>%
    mutate(plot_concentration = if_else(concentration_uM == 0, 0.001, concentration_uM)) %>%
    ggplot(aes(x = plot_concentration, y = mean_viability, color = drug_name)) +
    geom_line() +
    geom_point() +
    geom_errorbar(aes(ymin = mean_viability - sem_viability,
                      ymax = mean_viability + sem_viability), width = 0.05) +
    scale_x_log10() +
    labs(title = "Dose-Response Visualization",
         x = "Concentration (uM, log scale; 0 plotted as 0.001)",
         y = "Mean Cell Viability (%)")
}
