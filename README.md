# DSA 210 Project – April 14 Milestone

## Project Title

What Factors Affect Student Satisfaction and Migration Intentions?

---

## Project Description

This project aims to analyze the factors affecting student satisfaction using survey-based data. The focus is on understanding how different aspects such as academic experience, financial conditions, and social support influence overall satisfaction levels.

Additionally, the project explores the potential relationship between satisfaction and future intentions (e.g., staying or leaving), which will be further developed in later stages.

---

## Data Source

The dataset used in this project was obtained from publicly available sources (Kaggle student survey datasets). It contains information about students’ experiences, satisfaction levels, and related factors.

---

## Data Collection

The dataset was downloaded directly as a CSV file and cleaned using Python. Missing values and inconsistent data types were handled before analysis.

---

## Dataset Characteristics

The dataset includes variables such as:

* Satisfaction-related numeric scores
* Academic experience indicators
* Financial condition variables
* Social and environmental factors

The dataset contains multiple observations, allowing meaningful statistical analysis.

---

## Exploratory Data Analysis (EDA)

The following EDA steps were performed:

* Summary statistics calculation
* Distribution visualization using histograms
* Basic inspection of dataset structure

These steps helped to understand the distribution and variability of the key variables.

---

## Hypothesis Testing

To evaluate relationships between variables, statistical tests were applied:

* **ANOVA Test** was used to determine whether there are significant differences between groups

The results are stored in the repository as:

* `summary.csv`
* `results.json`
* `hist.png`

---

## Key Findings

* The distribution of the main variable was analyzed
* Group-based differences were tested using ANOVA
* Statistical significance was evaluated based on p-values

---

## Enrichment Plan

In accordance with the project guidelines, the dataset will be enriched in the next stage using external data sources such as country-level indicators (e.g., GDP per capita).

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* SciPy

---

## Repository Structure

```
.
├── data/
├── outputs/
│   ├── summary.csv
│   ├── results.json
│   └── hist.png
├── README.md
└── requirements.txt
```

---

## Reproducibility

To reproduce this analysis:

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Run the analysis script:

```
python src/april14_analysis.py
```

---

## AI Usage Disclosure

AI tools were used to assist with:

* project structuring
* code generation
* documentation

All final decisions and submissions were reviewed and completed by the student.

---
