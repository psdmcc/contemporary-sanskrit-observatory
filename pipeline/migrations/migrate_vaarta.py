#!/usr/bin/env python3
"""
Contemporary Sanskrit Observatory

Migration Script
================

Migration:
    Vārtā Corpus -> Observatory

Version:
    0.1

Purpose
-------
Reads the processed Vārtā corpus and validates that it is suitable for
migration into the Contemporary Sanskrit Observatory.

This version performs no writing.

It simply:

    1. Loads corpus_processed.csv
    2. Prints summary statistics
    3. Verifies required columns

Future versions will export:

    events.csv
    artifacts.csv
    documents.csv
"""

from pathlib import Path
import sys

import pandas as pd


# ---------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------

INPUT_FILE = Path("data/corpus_processed.csv")

REQUIRED_COLUMNS = [
    "video_id",
    "title",
    "published_at",
]


# ---------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------

def fail(message: str) -> None:
    """Print an error and exit."""
    print(f"\nERROR: {message}\n")
    sys.exit(1)


# ---------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------

def main():

    print("=" * 60)
    print("Contemporary Sanskrit Observatory")
    print("Vārtā Migration")
    print("=" * 60)

    if not INPUT_FILE.exists():
        fail(f"Cannot find input file:\n{INPUT_FILE}")

    print(f"\nLoading:\n{INPUT_FILE}\n")

    df = pd.read_csv(INPUT_FILE)

    print(f"Rows loaded : {len(df):,}")
    print(f"Columns     : {len(df.columns)}")

    print("\nChecking required columns...")

    missing = [
        column
        for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing:
        fail(f"Missing columns: {missing}")

    print("✓ All required columns present.")

    print("\nFirst columns:\n")

    for c in df.columns:
        print(f" - {c}")

    print("\nMigration validation successful.")


if __name__ == "__main__":
    main()
