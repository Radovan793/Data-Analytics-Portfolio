"""
Pandas Mini-Scripts for Dataset Manipulation

This script demonstrates common operations using pandas:
1️⃣ Filter rows & calculate new columns
2️⃣ Group & Aggregate
3️⃣ Sorting & Selecting Top N
4️⃣ Combining datasets (merge)
5️⃣ String manipulation
6️⃣ Applying a custom function
"""

import pandas as pd


def create_sample_data():
    """Create a sample employee dataset as a pandas DataFrame."""
    data = {
        "Name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
        "Age": [24, 30, 18, 35, 40],
        "Salary": [4000, 5000, 3000, 6000, 7000],
        "Department": ["HR", "IT", "IT", "Finance", "HR"]
    }
    return pd.DataFrame(data)


def filter_and_add_columns(df):
    """
    Filter employees older than 25 and add a YearlySalary column.
    
    Returns:
        older_than_25 (DataFrame): Employees older than 25
        df (DataFrame): Original df with new YearlySalary column
    """
    older_than_25 = df[df["Age"] > 25]
    df["YearlySalary"] = df["Salary"] * 12
    return older_than_25, df


def group_and_aggregate(df):
    """
    Group by Department and perform aggregations.
    
    Returns:
        dept_avg (DataFrame): Average salary per department
        dept_stats (DataFrame): Multiple aggregations per department
    """
    dept_avg = df.groupby("Department")["Salary"].mean().reset_index()
    dept_stats = df.groupby("Department").agg(
        avg_salary=("Salary", "mean"),
        max_age=("Age", "max"),
        min_age=("Age", "min")
    )
    return dept_avg, dept_stats


def sort_and_select_top(df, n=3):
    """Return top N employees by Salary."""
    return df.sort_values("Salary", ascending=False).head(n)


def combine_datasets(df):
    """Merge employee data with bonus data on Name."""
    bonus_data = {
        "Name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
        "Bonus": [500, 600, 300, 800, 700]
    }
    bonus_df = pd.DataFrame(bonus_data)
    combined_df = pd.merge(df, bonus_df, on="Name")
    return combined_df


def string_manipulation(df):
    """Extract first letter of Name and uppercase Department."""
    df["Initial"] = df["Name"].str[0]
    df["Department"] = df["Department"].str.upper()
    return df


def categorize_age(age):
    """Categorize age into Young, Mid-age, or Senior."""
    if age < 25:
        return "Young"
    elif age <= 35:
        return "Mid-age"
    else:
        return "Senior"


def apply_custom_function(df):
    """Apply categorize_age function to the Age column."""
    df["AgeGroup"] = df["Age"].apply(categorize_age)
    return df


if __name__ == "__main__":
    # Create sample data
    df = create_sample_data()

    # 1️⃣ Filter & Add Columns
    older_than_25, df = filter_and_add_columns(df)
    print("Employees older than 25:\n", older_than_25, "\n")
    print("Dataset with YearlySalary:\n", df, "\n")

    # 2️⃣ Group & Aggregate
    dept_avg, dept_stats = group_and_aggregate(df)
    print("Average salary per department:\n", dept_avg, "\n")
    print("Department statistics:\n", dept_stats, "\n")

    # 3️⃣ Sorting & Top N
    top_salary = sort_and_select_top(df, n=3)
    print("Top 3 salaries:\n", top_salary, "\n")

    # 4️⃣ Combine Datasets
    combined_df = combine_datasets(df)
    print("Combined dataset with bonuses:\n", combined_df, "\n")

    # 5️⃣ String Manipulation
    df = string_manipulation(df)
    print("String manipulation:\n", df, "\n")

    # 6️⃣ Apply Custom Function
    df = apply_custom_function(df)
    print("Dataset with AgeGroup:\n", df, "\n")