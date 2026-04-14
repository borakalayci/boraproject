# DSA 210 Project – April 14 Milestone Package

## Project Title
What Factors Affect International Students' Satisfaction and Migration Intentions?

## What this milestone covers
According to the course guideline, the April 14 deadline is for:
- data collection
- exploratory data analysis (EDA)
- hypothesis tests

This package gives you a clean repo structure and ready-to-use files for that milestone.

## Suggested repo structure
```text
.
├── data/
│   ├── raw/
│   │   └── put_your_main_dataset_here.csv
│   └── processed/
├── notebooks/
│   └── april14_milestone_analysis.ipynb   # optional, if you convert from the .py file
├── src/
│   └── april14_analysis.py
├── outputs/
│   └── figures/
├── README.md
├── requirements.txt
├── report_april14.md
├── ai_usage_disclosure.md
└── .gitignore
```

## Dataset strategy
Your proposal says you will use public survey-style data about international students and, if needed, combine or enrich it with additional sources.

The guideline also says that if you use a public dataset, you are expected to enrich it with another dataset.

### Recommended practical strategy
Use:
1. **One main student survey dataset**
   - should include satisfaction-related variables such as academic experience, housing, social life, finances, support, or well-being
   - if you find a dataset specifically for international students, use that first
   - if not, use a student satisfaction dataset and clearly state that the analysis is a proxy for international student experience until a more specific dataset is added

2. **One enrichment dataset**
   - add country-level or university-level context
   - examples:
     - GDP per capita from World Bank
     - education indicators from World Bank / UNESCO
     - cost-of-living or country-level development indicators

## What to do before submission
1. Put your CSV file into `data/raw/`
2. Rename it to `student_survey.csv`
3. Open `src/april14_analysis.py`
4. Adjust column names in the `CONFIG` section if needed
5. Run the script
6. Commit all outputs to GitHub

## Minimum GitHub commit suggestion
- commit 1: proposal + repo setup
- commit 2: raw data added
- commit 3: EDA notebook / script
- commit 4: hypothesis tests and report update

## Submission wording you can use
For the April 14 milestone, I completed the data collection phase, performed exploratory data analysis, and applied hypothesis tests on the dataset. I also enriched the public dataset with an additional external data source, in line with the course requirements.

## Important note
If your exact dataset does not contain a direct `migration_intention` column, you can still submit this milestone with:
- satisfaction analysis as the main track
- intention-to-stay / future-plan / study-abroad / career-plan variable as a proxy if available
- otherwise explicitly say migration intention modeling will be part of the next stage once the final dataset is finalized
