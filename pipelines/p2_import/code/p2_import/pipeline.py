from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from p2_import.config.ConfigStore import *
from p2_import.functions import *
from prophecy.utils import *
from p2_import.graph import *

def pipeline(spark: SparkSession) -> None:
    df_seed = seed(spark)
    df_Reformat_1 = Reformat_1(spark, df_seed)

def main():
    spark = SparkSession.builder.enableHiveSupport().appName("p2_import").getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/p2_import")
    spark.conf.set("spark.default.parallelism", "4")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/p2_import", config = Config)(pipeline)

if __name__ == "__main__":
    main()
