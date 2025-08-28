# Clean & Transform Client Transactions

## Objective
Prepare messy client transaction data for reliable financial analysis.

## Tools Used
- Python
- Pandas

## Skills Demonstrated
- Data wrangling
- Currency normalization
- Date parsing
- Transformation logic

## Source Data Challenges
| Issue | Examples |
|-------|---------|
| Inconsistent currency formats | EUR, eur, USD, GBP |
| Mixed date formats | 2024/12/01, 01-01-2025, 2025-01-05 |
| Inconsistent status values | Cleared, cleared, failed, pending |
| Missing essential values | NaN in amount or client_id |

## Step-by-Step Process
1. Load raw transaction data
2. Drop rows with missing `client_id` or `amount`
3. Clean column names
4. Standardize text values for `currency` and `status`
5. Parse mixed-format dates
6. Filter only 'cleared' transactions
7. Normalize all amounts to EUR
8. Reset index for tidy output
9. Optional: Save cleaned dataset

## Sample Output

| client_id | amount | currency | date       | status  | amount_eur |
|-----------|--------|----------|------------|---------|------------|
| 101       | 1200   | EUR      | 2024-12-01 | cleared | 1200.00    |
| 105       | 700    | EUR      | 2025-01-05 | cleared | 700.00     |

## Key Takeaways
- Applied data cleaning best practices on real-world messy data
- Standardized currencies and dates using `.apply()` and dictionaries
- Filtered and transformed data for valid financial records
- Delivered clean, structured output ready for downstream reporting


## PySpark Basics — Local DataFrame & Transformations

- Objective: Demonstrate PySpark initialization, DataFrame creation, and basic transformations for data engineering.
- Tools Used: Python, PySpark
- Skills Demonstrated: SparkSession setup, DataFrame creation, filtering, column transformations, handling duplicates, -- basic string operations, conditional logic, and reading/writing files.

## Process Steps & Logic:

- Initialize SparkSession
- Create a DataFrame from in-memory data
- Basic transformations: filter rows, add columns, drop duplicates
- String and conditional operations: .startswith(), .endswith(), .substr(), F.when(...).otherwise(...)
- Read/Write files: CSV, JSON, Parquet
- Explode nested arrays
- Filter with .isin() and .between()

Sample Output:

+---+-------+---+
| id|   name|age|
+---+-------+---+
|  1|  Alice| 28|
|  2|    Bob| 35|
|  3|Charlie| 25|
+---+-------+---+


## Key Takeaways:

- Able to set up PySpark locally and work with DataFrames
- Applied transformations, filters, and column operations efficiently
- Prepared for scalable ETL and data engineering workflows



