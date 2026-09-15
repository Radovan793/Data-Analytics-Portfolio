# Databricks notebook source
# Import required PySpark functions
from pyspark.sql.functions import (
    col,
    trim,
    upper,
    coalesce,
    try_to_date,
    isnan,
    when,
    sum,
    avg,
    count
)

# COMMAND ----------

# Read CSV file
df = spark.read.csv( 
    "/Volumes/workspace/default/customerdata", 
    header=True, 
    inferSchema=True
)
df.show()

# COMMAND ----------

# Inspect schema and sample records
df.printSchema()
df.show()

# COMMAND ----------

# Standardise Region values
df_clean = df.withColumn(
    "Region",
   upper(trim(col("Region")))
)
df_clean.show()


# COMMAND ----------

# Standardise different date formats
df_clean = df_clean.withColumn(
    "Sale_Date_Clean",
    coalesce(
        try_to_date(col("Sale_Date"), "yyyy-MM-dd"),
        try_to_date(col("Sale_Date"), "yyyy/MM/dd"),
        try_to_date(col("Sale_Date"), "MM-dd-yyyy")
    )
)
df_clean.show()

# COMMAND ----------

# Convert NaN values in Amount to NULL
df_clean = df_clean.withColumn(
    "Amount",
    when(isnan(col("Amount")), None)
    .otherwise(col("Amount"))
)
df_clean.show()

# COMMAND ----------

# Flag missing Amount values
df_clean = df_clean.withColumn(
    "Amount_Status",
    when(col("Amount").isNull(), "Missing")
    .otherwise("Valid")
)

df_clean.show()

# COMMAND ----------

# Calculate adjusted amounts and assign sales categories
df_new = (
    df_clean
    .withColumn(
        "Amount_with_discount", 
        col("Amount") * 0.9
    )
    .withColumn("Amount_extra_20%", 
        col("Amount") * 1.2
    )
    .withColumn(
        "Sales_Category",
        when(col("Amount").isNull(), "Missing") 
        .when(col("Amount") > 200, "High")
        .when(col("Amount") > 100, "Medium")
        .otherwise("Low")
    )
)
df_new.show()



# COMMAND ----------

# Check for duplicate records excluding Customer_ID
df_new.groupBy(
    [col for col in df_new.columns if col != "Customer_ID"]
).count().filter(
    col("count") > 1
).show()



# COMMAND ----------

# Remove duplicate records excluding Customer_ID
df_new_deduplicated = df_new.dropDuplicates(
    [col for col in df_new.columns if col != "Customer_ID"]
).orderBy("Customer_ID")

df_new_deduplicated.show()

# COMMAND ----------

# Calculate sales metrics by Region
df_agg = df_new_deduplicated.groupBy("Region") \
    .agg(
        sum("Amount").alias("Total_Sales"), 
        avg("Amount").alias("Avg_Sale"), 
        count("Amount").alias("Number_of_Sales")
    ) \
    .orderBy(col("Total_Sales").desc())

df_agg.show()


# COMMAND ----------

# Create regional manager reference data
df1 = spark.createDataFrame(
    [
        ("NORTH", "Manager A"),
        ("SOUTH", "Manager B"),
        ("EAST", "Manager C"),
        ("WEST", "Manager D")
    ],
    ["Region", "Manager"]
)

# Join manager information with regional sales
result_df = df_agg.join(df1, on='Region', how='inner')

result_df.show()