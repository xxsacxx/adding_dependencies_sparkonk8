from pyspark.sql import SparkSession
try:
    from functools import lru_cache
except ImportError:
    from backports.functools_lru_cache import lru_cache


@lru_cache(maxsize=None)
def get_spark():
    return (SparkSession.builder
                .master("local")
                .appName("gill")
                .getOrCreate())

