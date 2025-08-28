

# 1 Clean & Transform Client Transactions


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


  
# 2. PySpark Basics — Local DataFrame & Transformations

## Objective:
Demonstrate PySpark initialization, DataFrame creation, basic transformations, and queries for distributed data processing.

## Tools: Python, PySpark
Skills Demonstrated: SparkSession setup, DataFrame creation from local data, filtering, column transformations, handling duplicates, basic string functions, and conditional logic.

## Process Steps & Logic

## 1. Initialize SparkSession

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("PySparkPractice") \
    .master("local[*]") \
    .getOrCreate()


## 2. Create a DataFrame from in-memory data

data = [(1, "Alice", 28), (2, "Bob", 35), (3, "Charlie", 25)]
columns = ["id", "name", "age"]

df = spark.createDataFrame(data, columns)
df.show()


## 3. Basic Transformations

## Filter rows:

df.filter(df.age > 30).show()


## Add a column:

df.select(df.name, (df.age+1).alias("age_plus_one")).show()


## Drop duplicates:

df.dropDuplicates(["name"]).show()


## 4. String and Conditional Operations

.startswith(), .endswith(), .substr() on columns

## Conditional column creation:

from pyspark.sql import functions as F
df.select(df.name, F.when(df.age > 30, 1).otherwise(0).alias("over_30")).show()


## 5. Read / Write Files

## CSV:

df.write.csv("output_folder", header=True)


## JSON / Parquet:

df.write.parquet("output.parquet")


## 6. Explode Nested Arrays

df.select("name", F.explode(F.col("phoneNumber")).alias("contact")).show()


## 7. Filter with isin() and between()

df.filter(df.name.isin("Alice","Bob")).show()
df.filter(df.age.between(22,24)).show()

## Sample Output
+---+-------+---+
| id|   name|age|
+---+-------+---+
|  1|  Alice| 28|
|  2|    Bob| 35|
|  3|Charlie| 25|
+---+-------+---+

## Key Takeaways

- Set up PySpark locally and worked efficiently with DataFrames.
- Applied transformations, filters, and column operations.
- Demonstrated understanding of distributed data handling and file formats (CSV, JSON, Parquet).
- Prepared for scalable ETL and data engineering workflows.






