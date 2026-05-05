# DSA 210 Project

## Project Title
What Factors Affect International Students' Satisfaction and Migration Intentions?

---

## Dataset

**File:** `world_university_survey_dataset.csv`

**Variables (15 columns):**
- `student_id`, `student_name`, `age`, `gender`, `country`, `university`
- `program_level`, `field_of_study`, `year_of_study`
- `tuition_usd`, `scholarship`, `online_classes`
- `campus_facilities_rating`, `teaching_quality_rating`
- `overall_satisfaction` ← target variable

---

## Project Milestones

### ✅ Milestone 1 – Data Collection & EDA (April 14)

**What was done:**
- Dataset loaded and inspected (shape, dtypes, missing values)
- `overall_satisfaction` encoded into a numerical `satisfaction_score` (1–5 scale)
- Summary statistics and frequency distributions computed
- Visualizations produced: satisfaction distribution, age histogram, tuition histogram, top countries bar chart
- Group-level comparisons: satisfaction by scholarship status and by program level
- Correlation analysis across numerical variables

**Hypothesis Tests:**
| Test | Variables | Purpose |
|------|-----------|---------|
| Independent t-test (Welch) | Scholarship × satisfaction_score | Do scholarship recipients report higher satisfaction? |
| One-way ANOVA | Program level × satisfaction_score | Does satisfaction differ across program levels? |
| Chi-square test | overall_satisfaction × online_classes | Is there a relationship between modality and satisfaction? |

---

### ✅ Milestone 2 – Machine Learning (May 5)

**Task formulation:** Multi-class classification — predicting `overall_satisfaction` from student demographics, academic features, and ratings.

**Preprocessing:**
- Dropped `satisfaction_score` to prevent data leakage
- Label-encoded all categorical features (`country`, `gender`, `scholarship`, etc.)
- Standardized all features with `StandardScaler`
- 80/20 train-test split (random state = 42)

**Models trained:**

| Model | Type | Rationale |
|-------|------|-----------|
| Logistic Regression | Linear baseline | Fast, interpretable; benchmarks linear separability |
| Random Forest (100 trees) | Ensemble / non-linear | Captures complex feature interactions in survey data |

**Evaluation metrics:** Accuracy, Precision, Recall, F1-score (per class via `classification_report`)

**Key finding:** Model comparison revealed whether satisfaction is driven by linear patterns (favoring Logistic Regression) or complex feature interactions (favoring Random Forest). Results are visualized in a side-by-side accuracy bar chart.

---

## Repo Structure

```text
.
├── data/
│   ├── raw/
│   │   └── world_university_survey_dataset.csv
│   └── processed/
├── notebooks/
│   └── notebook.ipynb
├── outputs/
│   └── figures/
├── README.md
├── requirements.txt
└── .gitignore
```

## Requirements

```
pandas
numpy
matplotlib
seaborn
scipy
scikit-learn
```

---
