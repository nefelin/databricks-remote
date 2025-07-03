# Databricks notebook source
# COMMAND ----------
# This is the first cell

from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# Define schema
schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("name", StringType(), True)
])

# Create sample DataFrame
data = [(1, "Alice"), (2, "Bob"), (3, "Carol")]
df = spark.createDataFrame(data, schema)

# Write DataFrame to a table in the ericsandbox.default schema
df.write.mode("overwrite").saveAsTable("ericsandbox.default.git_notebook_table")
