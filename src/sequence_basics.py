"""Basic helpers for synthetic DNA sequence examples."""

import pandas as pd

DNA_COMPLEMENT = str.maketrans("ACGTacgt", "TGCAtgca")


def clean_sequence(sequence: str) -> str:
    """Return an uppercase sequence without spaces or line breaks."""
    return "".join(str(sequence).split()).upper()


def gc_content(sequence: str) -> float:
    """Calculate GC content as a percent."""
    seq = clean_sequence(sequence)
    if not seq:
        raise ValueError("sequence must not be empty.")
    gc = seq.count("G") + seq.count("C")
    return gc / len(seq) * 100


def reverse_complement(sequence: str) -> str:
    """Return the reverse complement of a DNA sequence."""
    seq = clean_sequence(sequence)
    invalid = set(seq) - set("ACGT")
    if invalid:
        raise ValueError(f"Invalid DNA bases: {sorted(invalid)}")
    return seq.translate(DNA_COMPLEMENT)[::-1]


def count_motif(sequence: str, motif: str) -> int:
    """Count non-overlapping motif occurrences in a DNA sequence."""
    seq = clean_sequence(sequence)
    motif = clean_sequence(motif)
    if not motif:
        raise ValueError("motif must not be empty.")
    return seq.count(motif)


def summarize_sequences(df: pd.DataFrame, sequence_col: str = "dna_sequence") -> pd.DataFrame:
    """Add length and GC-content summaries to a sequence table."""
    if sequence_col not in df.columns:
        raise ValueError(f"Missing required columns: {[sequence_col]}")
    result = df.copy()
    result["sequence_length"] = result[sequence_col].map(lambda seq: len(clean_sequence(seq)))
    result["gc_content_percent"] = result[sequence_col].map(gc_content)
    return result
