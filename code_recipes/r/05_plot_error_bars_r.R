library(ggplot2)

plot_group_means <- function(summary_df, group_col, mean_col, sem_col, title) {
  ggplot(summary_df, aes(x = .data[[group_col]], y = .data[[mean_col]])) +
    geom_col() +
    geom_errorbar(aes(
      ymin = .data[[mean_col]] - .data[[sem_col]],
      ymax = .data[[mean_col]] + .data[[sem_col]]
    ), width = 0.2) +
    labs(title = title)
}
