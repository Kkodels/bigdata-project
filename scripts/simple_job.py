from pyspark.sql import SparkSession

# Inisialisasi Spark
spark = SparkSession.builder \
    .appName("SimpleJob") \
    .getOrCreate()

# Data Dummy
data = [("A", 10), ("B", 20), ("A", 30)]
columns = ["category", "value"]

# Buat DataFrame
df = spark.createDataFrame(data, columns)

# Operasi Agregasi
df.groupBy("category").sum("value").show()

# Stop Spark
spark.stop()
