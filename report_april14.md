# April 14 Milestone Report

## Project
**What Factors Affect International Students' Satisfaction and Migration Intentions?**

## 1. Data collection
For this project, I used a publicly available student survey dataset and enriched it with an additional external data source, following the course guideline. The main dataset includes student-level variables related to satisfaction, living conditions, academic experience, finances, and social life. The enrichment step adds contextual indicators that can help explain variation across observations.

The data was downloaded from public online sources and then cleaned in Python. Missing values, inconsistent category labels, and data type issues were checked before the analysis stage.

## 2. Dataset characteristics
The dataset is expected to include:
- student-level satisfaction information
- academic experience variables
- housing / living condition variables
- social life variables
- financial variables
- if available, a future intention variable such as intention to stay, leave, or continue in the host country

The exact number of observations and variables will depend on the final selected dataset. This information should be updated after loading the dataset.

## 3. Exploratory Data Analysis
The exploratory data analysis focuses on understanding the distribution of satisfaction and its relationship with important explanatory variables.

Planned EDA steps:
- summary statistics for numeric variables
- frequency tables for categorical variables
- missing value inspection
- histogram of satisfaction
- boxplots of satisfaction across groups
- correlation analysis for numeric predictors

These steps help identify the structure of the data, detect outliers, and guide the choice of hypothesis tests.

## 4. Hypothesis tests
The following hypotheses are appropriate for this milestone:

### Hypothesis 1
**H0:** Mean satisfaction does not differ between students with good housing conditions and poor housing conditions.  
**H1:** Mean satisfaction differs between these two groups.

Suggested test: independent samples t-test

### Hypothesis 2
**H0:** Satisfaction is independent of financial difficulty level.  
**H1:** Satisfaction differs across financial difficulty groups.

Suggested test: one-way ANOVA if there are more than two groups

### Hypothesis 3
**H0:** There is no association between social support and migration intention.  
**H1:** There is an association between social support and migration intention.

Suggested test: chi-square test of independence  
If migration intention is not available, this hypothesis can be replaced with another categorical outcome.

## 5. Current findings
This section should be updated after running the analysis script. A good short version is:

- The dataset was collected and cleaned successfully.
- Initial visualizations show how satisfaction changes across key factors such as housing, finances, and academic experience.
- Hypothesis tests were applied to evaluate whether these observed differences are statistically meaningful.

## 6. Limitations
A limitation at this stage is that publicly available datasets may not perfectly capture international student migration intentions. Some variables may need to be approximated by closely related indicators, and the final machine learning stage may require additional feature engineering or dataset enrichment.

## 7. Next step
For the May 5 milestone, machine learning methods will be applied to predict satisfaction and, if available, migration intention using the cleaned and enriched dataset.
