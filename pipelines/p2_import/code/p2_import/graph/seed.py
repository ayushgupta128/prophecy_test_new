from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from p2_import.config.ConfigStore import *
from p2_import.functions import *

def seed(spark: SparkSession) -> DataFrame:
    return spark.read.option("header", True).option("sep", ",").csv("")
