# Week 5 — Pandas for QA Engineers

## Pages Read
- Pandas Official Docs: Getting Started (Tutorials 1–3)
- Pandas IO Tools (Reading/Writing)
- Pandas Indexing & Selecting Data
- Pandas Missing Data Guide
- Pandas GroupBy Guide
- W3Schools Pandas Series

## Exercises Done
- **Day 1:** pandas_intro.py → Series & DataFrames basics
- **Day 2:** pandas_io.py → CSV/JSON read & write
- **Day 3:** pandas_filter.py → Filtering with conditions, loc/iloc
- **Day 4:** pandas_clean.py → Handling nulls, filling, dropping
- **Day 5:** pandas_analyze.py → Summaries & group by
- **Day 6:** qa_dataset_explorer.py → Mini QA dataset explorer

## 3 Code Snippets I’m Proud Of

### 1. Value Counts for Quick QA Checks
```python
reader["email"].value_counts(dropna=False).head(5)
```
*Fast way to see top email providers, including missing values.*

### 2. Group By and Mean
```python
summary = (
    reader.groupby("sound_waveform")["color_saturation"]
    .mean()
    .reset_index()
)
```
*Shows average values per category in a clean, readable format.*

### 3. Mini Explorer Dictionary Export
```python
combined = {
    "shape": {"rows": shape[0], "columns": shape[1]},
    "columns": columns,
    "empty cells": null_count,
    "selected column": chosen_column,
    "top values": result
}
```
*Structured summary of dataset → easy to export to JSON for QA reports.*

---

## Journal Reflection
**How does pandas change the way I think about CSV/JSON?**  

## Journal Reflection
**How does pandas change the way I think about CSV/JSON?**

Pandas feels a lot easier to use than working directly with CSV or JSON. I was surprised by how simple things were once I used its functions. Tasks that felt awkward before became straightforward, and the syntax itself felt more intuitive. It made me realize that at the core, this is all just data — and pandas is powerful because it can access and present that data in a more essential way. Instead of fighting the structure of CSV/JSON with loops and conditionals, pandas lets me explore, clean, and summarize data with single, expressive commands. That makes the whole process feel less like manual work and more like analysis.


---
