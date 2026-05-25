library(tidyverse)

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
