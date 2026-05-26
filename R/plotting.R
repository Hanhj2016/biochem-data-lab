library(tidyverse)

# Reusable ggplot2 helpers for synthetic Biochemistry teaching datasets.

require_columns <- function(df, columns) {
  missing <- setdiff(columns, names(df))
  if (length(missing) > 0) {
    stop(paste("Missing required columns:", paste(missing, collapse = ", ")))
  }
}

plot_group_means <- function(summary_df, group_col, mean_col, sem_col, title) {
  require_columns(summary_df, c(group_col, mean_col, sem_col))

  ggplot(summary_df, aes(x = .data[[group_col]], y = .data[[mean_col]])) +
    geom_col() +
    geom_errorbar(aes(
      ymin = .data[[mean_col]] - .data[[sem_col]],
      ymax = .data[[mean_col]] + .data[[sem_col]]
    ), width = 0.2) +
    labs(title = title)
}

plot_dose_response <- function(summary_df) {
  require_columns(summary_df, c("drug_name", "concentration_uM", "mean_viability", "sem_viability"))

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

plot_heatmap <- function(expr_df) {
  if (nrow(expr_df) == 0 || ncol(expr_df) == 0) {
    stop("expr_df must contain genes as rows and samples as columns")
  }

  expr_z <- t(scale(t(as.matrix(expr_df))))
  heatmap_df <- as.data.frame(expr_z) %>%
    mutate(gene = rownames(expr_z)) %>%
    pivot_longer(-gene, names_to = "sample", values_to = "z_score")

  ggplot(heatmap_df, aes(x = sample, y = gene, fill = z_score)) +
    geom_tile() +
    labs(title = "Gene Expression Heatmap")
}

make_pca_sample_scores <- function(expr_df) {
  if (nrow(expr_df) == 0 || ncol(expr_df) < 2) {
    stop("expr_df must contain genes as rows and at least two sample columns")
  }

  pca <- prcomp(t(expr_df), scale. = TRUE)
  as.data.frame(pca$x[, 1:2]) %>%
    mutate(sample = rownames(pca$x)) %>%
    mutate(group = str_extract(sample, "control|treat_low|treat_high|treatment"))
}

plot_pca_sample_map <- function(pca_df) {
  require_columns(pca_df, c("sample", "PC1", "PC2"))

  ggplot(pca_df, aes(x = PC1, y = PC2, color = group, label = sample)) +
    geom_point(size = 3) +
    geom_text(vjust = -0.8) +
    labs(title = "Toy PCA Sample Map")
}
