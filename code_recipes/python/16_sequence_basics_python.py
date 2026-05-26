import pandas as pd

from src.sequence_basics import count_motif, reverse_complement, summarize_sequences

df = pd.read_csv("data/sequences/synthetic_sequences.csv")
summary = summarize_sequences(df)
summary["ATG_count"] = summary["dna_sequence"].map(lambda seq: count_motif(seq, "ATG"))
summary["reverse_complement"] = summary["dna_sequence"].map(reverse_complement)

print(summary[["sequence_id", "sequence_length", "gc_content_percent", "ATG_count"]])
