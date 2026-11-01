#!/usr/bin/env python3
"""Organize a simple song catalog CSV.

Input CSV columns: title,artist,language
Usage: python3 main.py songs.csv
"""
import csv
import sys
from collections import Counter

def main(path):
    with open(path, newline='', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))
    print(f"Total songs: {len(rows)}")
    print("By language:", dict(Counter(r.get("language", "") for r in rows)))
    for r in rows:
        print(f"- {r.get('title','')} ({r.get('artist','')})")

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "songs.csv")
