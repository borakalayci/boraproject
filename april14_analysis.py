"""
DSA 210 – April 14 milestone
Data collection + EDA + hypothesis tests

How to use:
1. Put your dataset at: data/raw/student_survey.csv
2. Update CONFIG below to match your column names
3. Run: python src/april14_analysis.py

This script is intentionally flexible because your final dataset may differ.
"""

from pathlib import Path
import json
import warnings

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

warnings.filterwarnings("ignore")

# ----------------------------
# CONFIG: CHANGE THESE NAMES
# ----------------------------
CONFIG = {
    "file_path": "data/raw/student_survey.csv",

    # outcome column
    "satisfaction_col": "satisfaction",

    # candidate explanatory columns
    "housing_col": "housing_condition",
    "finance_col": "financial_difficulty",
    "social_support_col": "social_support",
    "migration_col": "migration_intention",

    # optional grouping column
    "region_col": "region",

    # values for binary/grouped tests
    "good_housing_values": ["good", "very good", "satisfied", "high"],
    "poor_housing_values": ["poor", "very poor", "unsatisfied", "low"],
}

ROOT = Path(".")
OUTPUT_DIR = ROOT / "outputs"
FIG_DIR = OUTPUT_DIR / "figures"
PROC_DIR = ROOT / "data" / "processed"

OUTPUT_DIR.mkdir(exist_ok=True, parents=True)
FIG_DIR.mkdir(exist_ok=True, parents=True)
PROC_DIR.mkdir(exist_ok=True, parents=True)


def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df


def standardize_strings(df: pd.DataFrame) -> pd.DataFrame:
    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].astype(str).str.strip()
    return df


def basic_cleaning(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = standardize_strings(df)

    # try to convert numeric-looking columns
    for col in df.columns:
        try:
            converted = pd.to_numeric(df[col])
            # only replace if it does not create too many NaNs
            if converted.notna().mean() > 0.8:
                df[col] = converted
        except Exception:
            pass
    return df


def summary_tables(df: pd.DataFrame) -> None:
    desc = df.describe(include="all").transpose()
    desc.to_csv(OUTPUT_DIR / "summary_statistics.csv")

    missing = (
        df.isna()
        .sum()
        .rename("missing_count")
        .to_frame()
        .assign(missing_rate=lambda x: x["missing_count"] / len(df))
    )
    missing.to_csv(OUTPUT_DIR / "missing_values.csv")


def plot_histogram(df: pd.DataFrame, col: str) -> None:
    if col in df.columns and pd.api.types.is_numeric_dtype(df[col]):
        plt.figure(figsize=(7, 4))
        df[col].dropna().hist(bins=20)
        plt.title(f"Distribution of {col}")
        plt.xlabel(col)
        plt.ylabel("Frequency")
        plt.tight_layout()
        plt.savefig(FIG_DIR / f"{col}_histogram.png", dpi=200)
        plt.close()


def plot_boxplot(df: pd.DataFrame, y_col: str, group_col: str) -> None:
    if y_col in df.columns and group_col in df.columns:
        temp = df[[y_col, group_col]].dropna()
        if len(temp) == 0:
            return
        groups = [g[y_col].values for _, g in temp.groupby(group_col)]
        labels = list(temp[group_col].dropna().unique())
        if len(groups) >= 2:
            plt.figure(figsize=(8, 4))
            plt.boxplot(groups, tick_labels=labels)
            plt.title(f"{y_col} by {group_col}")
            plt.xlabel(group_col)
            plt.ylabel(y_col)
            plt.xticks(rotation=30, ha="right")
            plt.tight_layout()
            plt.savefig(FIG_DIR / f"{y_col}_by_{group_col}_boxplot.png", dpi=200)
            plt.close()


def correlation_table(df: pd.DataFrame) -> None:
    numeric_df = df.select_dtypes(include=[np.number])
    if numeric_df.shape[1] >= 2:
        corr = numeric_df.corr(numeric_only=True)
        corr.to_csv(OUTPUT_DIR / "correlation_matrix.csv")


def two_group_ttest(df: pd.DataFrame, y_col: str, group_col: str, good_vals, poor_vals):
    if y_col not in df.columns or group_col not in df.columns:
        return {"status": "skipped", "reason": "columns not found"}

    temp = df[[y_col, group_col]].dropna().copy()
    if temp.empty:
        return {"status": "skipped", "reason": "no data after dropping NA"}

    temp[group_col] = temp[group_col].astype(str).str.lower()

    good = temp[temp[group_col].isin([str(v).lower() for v in good_vals])][y_col]
    poor = temp[temp[group_col].isin([str(v).lower() for v in poor_vals])][y_col]

    if len(good) < 2 or len(poor) < 2:
        return {"status": "skipped", "reason": "not enough observations in two groups"}

    stat, p = stats.ttest_ind(good, poor, equal_var=False, nan_policy="omit")
    return {
        "status": "ok",
        "test": "Welch t-test",
        "group_1_n": int(len(good)),
        "group_2_n": int(len(poor)),
        "group_1_mean": float(np.mean(good)),
        "group_2_mean": float(np.mean(poor)),
        "t_stat": float(stat),
        "p_value": float(p),
    }


def anova_test(df: pd.DataFrame, y_col: str, group_col: str):
    if y_col not in df.columns or group_col not in df.columns:
        return {"status": "skipped", "reason": "columns not found"}

    temp = df[[y_col, group_col]].dropna().copy()
    if temp.empty:
        return {"status": "skipped", "reason": "no data after dropping NA"}

    grouped = [g[y_col].values for _, g in temp.groupby(group_col)]
    if len(grouped) < 2 or any(len(g) < 2 for g in grouped):
        return {"status": "skipped", "reason": "not enough groups/observations"}

    stat, p = stats.f_oneway(*grouped)
    return {
        "status": "ok",
        "test": "One-way ANOVA",
        "num_groups": int(len(grouped)),
        "f_stat": float(stat),
        "p_value": float(p),
    }


def chi_square_test(df: pd.DataFrame, col1: str, col2: str):
    if col1 not in df.columns or col2 not in df.columns:
        return {"status": "skipped", "reason": "columns not found"}

    temp = df[[col1, col2]].dropna().copy()
    if temp.empty:
        return {"status": "skipped", "reason": "no data after dropping NA"}

    table = pd.crosstab(temp[col1], temp[col2])
    if table.shape[0] < 2 or table.shape[1] < 2:
        return {"status": "skipped", "reason": "contingency table too small"}

    chi2, p, dof, expected = stats.chi2_contingency(table)
    table.to_csv(OUTPUT_DIR / f"crosstab_{col1}_vs_{col2}.csv")
    return {
        "status": "ok",
        "test": "Chi-square test of independence",
        "chi2_stat": float(chi2),
        "p_value": float(p),
        "dof": int(dof),
    }


def interpret_pvalue(p):
    if p < 0.01:
        return "strong evidence against H0"
    if p < 0.05:
        return "evidence against H0"
    return "not enough evidence against H0"


def main():
    file_path = CONFIG["file_path"]
    if not Path(file_path).exists():
        raise FileNotFoundError(
            f"Dataset not found at {file_path}. Put your CSV there and rename it to student_survey.csv"
        )

    df = load_data(file_path)
    df = basic_cleaning(df)
    df.to_csv(PROC_DIR / "cleaned_student_survey.csv", index=False)

    summary_tables(df)
    correlation_table(df)

    satisfaction_col = CONFIG["satisfaction_col"]
    housing_col = CONFIG["housing_col"]
    finance_col = CONFIG["finance_col"]
    social_support_col = CONFIG["social_support_col"]
    migration_col = CONFIG["migration_col"]

    plot_histogram(df, satisfaction_col)
    plot_boxplot(df, satisfaction_col, housing_col)
    plot_boxplot(df, satisfaction_col, finance_col)

    results = {}

    results["hypothesis_1_housing_vs_satisfaction"] = two_group_ttest(
        df,
        y_col=satisfaction_col,
        group_col=housing_col,
        good_vals=CONFIG["good_housing_values"],
        poor_vals=CONFIG["poor_housing_values"],
    )

    results["hypothesis_2_finance_vs_satisfaction"] = anova_test(
        df,
        y_col=satisfaction_col,
        group_col=finance_col,
    )

    results["hypothesis_3_social_support_vs_migration"] = chi_square_test(
        df,
        col1=social_support_col,
        col2=migration_col,
    )

    # add simple interpretations
    for key, value in results.items():
        if value.get("status") == "ok":
            value["interpretation"] = interpret_pvalue(value["p_value"])

    with open(OUTPUT_DIR / "hypothesis_test_results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    # also save a markdown summary
    lines = ["# Hypothesis Test Results", ""]
    for name, res in results.items():
        lines.append(f"## {name}")
        if res.get("status") != "ok":
            lines.append(f"- Skipped: {res.get('reason')}")
        else:
            for k, v in res.items():
                lines.append(f"- {k}: {v}")
        lines.append("")

    with open(OUTPUT_DIR / "hypothesis_test_results.md", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print("Done. Outputs saved to:")
    print("- outputs/")
    print("- outputs/figures/")
    print("- data/processed/")


if __name__ == "__main__":
    main()
