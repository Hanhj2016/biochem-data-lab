library(tidyverse)

# Load a synthetic gene expression matrix.
# Rows are genes; columns are samples.
df <- read_csv("data/gene_expression/gene_expression_matrix_pca.csv")

expr <- df
rownames(expr) <- expr$gene
expr <- expr %>% select(-gene)

# PCA with base R prcomp.
# Samples should be rows and genes should be columns.
pca <- prcomp(t(expr), scale. = TRUE)

pca_df <- as.data.frame(pca$x[, 1:2]) %>%
  mutate(sample = rownames(pca$x)) %>%
  mutate(group = str_extract(sample, "control|treat_low|treat_high"))

ggplot(pca_df, aes(x = PC1, y = PC2, color = group, label = sample)) +
  geom_point(size = 3) +
  geom_text(vjust = -0.8) +
  labs(title = "Toy PCA Sample Map")
