library(tidyverse)

# Basic helpers for synthetic DNA sequence examples.

clean_sequence <- function(sequence) {
  toupper(gsub("\\s+", "", as.character(sequence)))
}

gc_content <- function(sequence) {
  seq <- clean_sequence(sequence)
  if (nchar(seq) == 0) {
    stop("sequence must not be empty")
  }
  chars <- strsplit(seq, "")[[1]]
  (sum(chars %in% c("G", "C")) / length(chars)) * 100
}

count_motif <- function(sequence, motif) {
  seq <- clean_sequence(sequence)
  motif <- clean_sequence(motif)
  if (nchar(motif) == 0) {
    stop("motif must not be empty")
  }
  stringr::str_count(seq, fixed(motif))
}

reverse_complement <- function(sequence) {
  seq <- clean_sequence(sequence)
  invalid <- setdiff(strsplit(seq, "")[[1]], c("A", "C", "G", "T"))
  if (length(invalid) > 0) {
    stop(paste("Invalid DNA bases:", paste(unique(invalid), collapse = ", ")))
  }
  comp <- chartr("ACGT", "TGCA", seq)
  paste(rev(strsplit(comp, "")[[1]]), collapse = "")
}

summarize_sequences <- function(df, sequence_col = "dna_sequence") {
  if (!sequence_col %in% names(df)) {
    stop(paste("Missing required columns:", sequence_col))
  }
  df %>%
    mutate(
      sequence_length = nchar(map_chr(.data[[sequence_col]], clean_sequence)),
      gc_content_percent = map_dbl(.data[[sequence_col]], gc_content)
    )
}
