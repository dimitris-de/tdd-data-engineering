import unittest
from src.Ex_9_spark_jobs import process_data
from pyspark.sql import SparkSession


class TestSparkJobs(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Initialize SparkSession for all tests.
        """
        cls.spark = SparkSession.builder \
            .master("local[1]") \
            .appName("SparkUnitTest") \
            .getOrCreate()

    @classmethod
    def tearDownClass(cls):
        """
        Stop SparkSession after all tests.
        """
        cls.spark.stop()

    def test_process_data(self):
        """
        Test the process_data function.
        """
        input_data = self.spark.createDataFrame(
            [('Alice', 1000), ('Bob', 2000)],
            ['name', 'salary']
        )
        result = process_data(input_data)
        expected_data = self.spark.createDataFrame(
            [('Alice', 1100), ('Bob', 2200)],
            ['name', 'new_salary']
        )
        self.assertEqual(sorted(result.collect()), sorted(expected_data.collect()))

if __name__ == '__main__':
    unittest.main()
