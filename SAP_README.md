# Student Score Analyzer 📊

A data analysis project built with **Python, Pandas, NumPy, and Matplotlib** that performs end-to-end analysis on a student dataset — from raw messy data to insights and visualizations.

Built as a hands-on practice project to solidify core data science skills before moving into Machine Learning.

---

## What this project does

- Generates a realistic student dataset (200 students, intentional missing values & noise)
- Cleans and preprocesses the data — handles nulls, duplicates, type conversions
- Engineers new features — grade classification, pass/fail labels
- Performs full Exploratory Data Analysis (EDA)
- Uses NumPy for array operations, normalization, and statistical analysis
- Visualizes key insights with Matplotlib

---

## Concepts practiced

| Library | Concepts |
|---------|----------|
| **Pandas** | `read_csv`, `fillna`, `dropna`, `astype`, `drop_duplicates`, `groupby`, `apply`, `merge`, `pivot_table`, `nlargest`, `value_counts`, `sort_values`, `corr` |
| **NumPy** | Array creation, `np.where`, `np.percentile`, `np.clip`, `reshape`, `axis`, boolean masking, `np.random`, vectorized math |
| **Matplotlib** | Histograms, bar charts, figure sizing, labels, titles |

---

## Project structure

```
student-score-analyzer/
│
├── student_project.py      # Main analysis script
├── students.csv            # Auto-generated dataset (created on first run)
├── README.md               # This file
```

---

## How to run it

**1. Clone the repo**
```bash
git clone https://github.com/YOUR_USERNAME/student-score-analyzer.git
cd student-score-analyzer
```

**2. Install dependencies**
```bash
pip install pandas numpy matplotlib
```

**3. Run the script**
```bash
python student_project.py
```

The script auto-generates `students.csv` on first run — no need to download any data.

---

## Sample output

**Grade distribution across students:**

| Grade | Count |
|-------|-------|
| A (>80) | ~35 students |
| B (>70) | ~40 students |
| C (>60) | ~45 students |
| D (<60) | ~70 students |

**Key insights extracted:**
- Average marks per subject (via `groupby`)
- Top 5 students by marks
- Marks vs Attendance correlation
- Pass/Fail breakdown using `np.where`
- City-wise student count

---

## Key code snippets

**Handling missing data:**
```python
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df = df.dropna(subset=["Attendance"])
```

**Feature engineering with apply():**
```python
def grade(m):
    if m > 80: return "A"
    elif m > 70: return "B"
    elif m > 60: return "C"
    else: return "D"

df["Grade"] = df["Marks"].apply(grade)
```

**NumPy normalization (min-max scaling):**
```python
marks = df["Marks"].values
normalized = (marks - np.min(marks)) / (np.max(marks) - np.min(marks))
```

**Pivot table:**
```python
pivot = pd.pivot_table(df, values="Marks", index="City", columns="Subject", aggfunc="mean")
```

---

## What I'm working on next

- [ ] Scikit-learn — train a classification model to predict Pass/Fail
- [ ] Add Seaborn visualizations (heatmap, pairplot)
- [ ] PyTorch — build a neural network on this dataset

---

## Author

**[Your Name]** — currently learning ML/DL Engineering

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://linkedin.com/in/YOUR_PROFILE)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black)](https://github.com/YOUR_USERNAME)
