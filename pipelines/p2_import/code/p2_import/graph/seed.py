from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from p2_import.config.ConfigStore import *
from p2_import.functions import *

def seed(spark: SparkSession) -> DataFrame:
    schemaFields = StructType([StructField("id", StringType(), True), StructField("age", StringType(), True)]).fields
    readSchema = StructType([StructField(f.name, StringType(), True) for f in schemaFields])

    return spark.createDataFrame([Row("1", "1"), Row("2", "2"), Row("3", "3"), Row("4", "4")], readSchema)
