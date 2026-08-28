"""Spark transformation jobs"""
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, hour, dayofweek, when


def create_spark_session(app_name: str = "DataTransformation") -> SparkSession:
    return SparkSession.builder \
        .appName(app_name) \
        .config("spark.sql.warehouse.dir", "/user/hive/warehouse") \
        .getOrCreate()


def transform_transactions(spark: SparkSession, input_path: str) -> DataFrame:
    df = spark.read.parquet(input_path)
    
    transformed = df \
        .withColumn("hour", hour(col("timestamp"))) \
        .withColumn("day_of_week", dayofweek(col("timestamp"))) \
        .withColumn("is_weekend", when(col("day_of_week").isin(1, 7), 1).otherwise(0)) \
        .withColumn("amount_category", 
            when(col("amount") < 100, "low")
            .when(col("amount") < 1000, "medium")
            .otherwise("high"))
    
    return transformed
