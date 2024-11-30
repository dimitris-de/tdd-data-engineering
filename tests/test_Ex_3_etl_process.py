import unittest
from src.Ex_3_etl_process import extract_data, load_data, transform_data, validate_data

class TestETLProcess(unittest.TestCase):
    def test_etl_pipeline(self):
        """
        Test the end-to-end ETL pipeline.
        """
        # Simulate extraction
        raw_data = extract_data('data/input.csv')
        self.assertGreater(len(raw_data), 0)

        # Simulate transformation
        transformed_data = transform_data(raw_data)
        self.assertIn('normalized_value', transformed_data[0])

        # Simulate loading
        result = load_data(transformed_data, 'data/output.csv')
        self.assertTrue(result)


    def test_validate_data_with_invalid_age(self):
        """
        Test that validate_data raises ValueError for invalid 'age'.
        """
        data = {'name': 'John Doe', 'age': 'twenty'}
        with self.assertRaises(ValueError):
            validate_data(data)


    def test_validate_data_missing_name(self):
        """
        Test that validate_data raises KeyError when 'name' is missing.
        """
        data = {'age': '30'}
        with self.assertRaises(KeyError):
            validate_data(data)

if __name__ == '__main__':
    unittest.main()
