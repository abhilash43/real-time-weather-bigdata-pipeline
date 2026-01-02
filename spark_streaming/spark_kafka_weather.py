from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, DoubleType

# Spark session
spark = SparkSession.builder \
    .appName("KafkaWeatherStreaming") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# Schema matching Kafka messages
schema = StructType([
    StructField("temperature", DoubleType(), True),
    StructField("humidity", DoubleType(), True),
    StructField("wind", DoubleType(), True),
    StructField("timestamp", StringType(), True)
])

# Read from Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "weather") \
    .option("startingOffsets", "earliest") \
    .load()

# Parse JSON
json_df = df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

# Write to console (for validation)
query = json_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .option("truncate", "false") \
    .start()

query.awaitTermination()
