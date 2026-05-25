library(tidyverse)

# expr should be a matrix with genes as rows and samples as columns.
plot_expression_heatmap <- function(expr) {
  expr_z <- t(scale(t(as.matrix(expr))))
  heatmap_df <- as.data.frame(expr_z) %>%
    rownames_to_column("gene") %>%
    pivot_longer(-gene, names_to = "sample", values_to = "z_score")

  ggplot(heatmap_df, aes(x = sample, y = gene, fill = z_score)) +
    geom_tile() +
    labs(title = "Gene Expression Heatmap") +
    theme(axis.text.x = element_text(angle = 45, hjust = 1))
}
