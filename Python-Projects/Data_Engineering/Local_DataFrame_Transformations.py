# PySpark Basics — Local DataFrame & Transformations
# Objective: Demonstrate PySpark initialization, DataFrame creation, transformations, and queries.

from pyspark.sql import SparkSession, functions as F


# ---------------- Initialize SparkSession ----------------
spark = SparkSession.builder \
    .appName("PySparkPractice") \
    .master("local[*]") \
    .getOrCreate()


# ---------------- Create DataFrame from in-memory data ----------------
data = [(1, "Alice", 28), (2, "Bob", 35), (3, "Charlie", 25)]
columns = ["id", "name", "age"]
df = spark.createDataFrame(data, columns)

print("=== Original Data ===")
df.show()


# ---------------- Basic Transformations ----------------
print("=== Filter age > 30 ===")
df.filter(df.age > 30).show()

print("=== Add 1 to age ===")
df.select(df.name, (df.age + 1).alias("age_plus_one")).show()

print("=== Drop duplicates on name ===")
df.dropDuplicates(["name"]).show()


# ---------------- String and Conditional Operations ----------------
print("=== Example startswith, endswith, substring ===")
df.select(
    df.name,
    df.name.startswith("A").alias("starts_with_A"),
    df.name.endswith("e").alias("ends_with_e"),
    df.name.substr(1, 3).alias("first3chars")
).show()

print("=== Conditional column: age > 30 ===")
df.select(
    "name",
    F.when(df.age > 30, 1).otherwise(0).alias("over_30")
).show()


# ---------------- Read/Write files ----------------
# Example placeholders (uncomment and set paths if needed)
# df.write.csv("output_folder", header=True)
# df.write.parquet("output.parquet")


# ---------------- Filter with isin() and between() ----------------
print("=== Filter names Alice or Bob ===")
df.filter(df.name.isin("Alice", "Bob")).show()

print("=== Filter age between 22 and 30 ===")
df.filter(df.age.between(22, 30)).show()

# Stop Spark
spark.stop()
