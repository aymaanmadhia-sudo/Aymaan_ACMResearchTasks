# Aymaan_ACMResearchTasks

This repo contains my submission for the DJSCE ACM Student Chapter Research
Task.

## Contents

- **task0/** — `transform_logs.py`: a Python function `transform_logs()`
  that cleans up messy log text by hiding emails, hiding IPv4 addresses,
  normalizing timestamps into a readable format, and identifying every
  `ERROR` occurrence .
- **task1/** — `blog_review.md`: review of "Deep Learning (Part 1):
  Understanding Basic Neural Networks" by Lindah Sumbati.
- **task2/** — `paper_summary.md`: summary of "How to Read a Paper" by
  S. Keshav, and how I plan to apply the three-pass method.
- **bonus/** - `eda.ipynb`: Exploratory Data Analysis (EDA) on the NHANES health survey dataset used for Age Group Prediction (Adult vs Senior). Includes data loading, data inspection, visualization, and feature analysis.

## How to run Task 0

Requires Python 3.8+

```bash
cd task0
python3 transform_logs.py
```

This runs the built-in test cases and prints the input/output for each.
you can even use it on your own text after two text.

