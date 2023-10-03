from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create a Spark session
spark = SparkSession.builder.appName("SamplePySpark").getOrCreate()

# Reading CSV files into DataFrames
df1 = spark.read.csv("path/to/df1.csv", header=True, inferSchema=True)
df2 = spark.read.csv("path/to/df2.csv", header=True, inferSchema=True)

# Joining DataFrames
joined_df = df1.join(df2, on="common_column", how="inner")

# Grouping and Aggregating
grouped_df = joined_df.groupBy("grouping_column").agg({"agg_column": "sum"})

# Filtering
filtered_df = grouped_df.filter(col("agg_column") > 1000)

# Writing the result to an output file (e.g., Parquet format)
output_path = "path/to/output"
filtered_df.write.mode("overwrite").parquet(output_path)

# Stop the Spark session
spark.stop()
