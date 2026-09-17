# PySpark CSV ETL Pipeline

A simple data engineering project built with **PySpark in Databricks**. The pipeline reads customer sales data from CSV, performs data cleaning and transformation, removes duplicate records, calculates sales metrics, and enriches the results with regional manager information.

## Technologies

- Python
- PySpark
- Databricks
- CSV

## Project Overview

The pipeline demonstrates a basic ETL workflow:

1. Read customer sales data from CSV
2. Inspect the data and schema
3. Standardise region values
4. Standardise inconsistent date formats
5. Handle missing and invalid sales amounts
6. Create derived columns and sales categories
7. Identify duplicate records
8. Remove duplicate records
9. Calculate sales metrics by region
10. Join sales results with regional manager data

## Data Cleaning

The source data contains several data quality issues that are intentionally included for demonstration:

- Inconsistent capitalisation and whitespace in region names
- Multiple date formats
- Missing and `NaN` values in the sales amount
- Duplicate records

The pipeline standardises these values before performing the analysis.

## Transformations

The pipeline creates several additional fields:

- `Sale_Date_Clean` – standardised date field
- `Amount_Status` – identifies missing sales amounts
- `Amount_with_discount` – sales amount after a 10% discount
- `Amount_extra_20%` – sales amount increased by 20%
- `Sales_Category` – classifies sales as High, Medium, Low, or Missing

## Aggregation

Sales are aggregated by region using:

- Total sales
- Average sale amount
- Number of sales

The aggregated results are then joined with a small regional manager reference dataset.

## Environment

The pipeline was developed and tested in Databricks using PySpark.

The source data was loaded from a Databricks Volume:

```text
/Volumes/workspace/default/customerdata
```

A copy of the source dataset is included in this repository as `sales_data.csv` for reference.

## Project Files

```text
ETL project/
├── CSV_ETL_Pipeline_PySpark.py
├── sales_data.csv
└── README_CSV_ETL_PySpark.md
```