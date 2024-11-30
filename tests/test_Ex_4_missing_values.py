import unittest
from src.Ex_4_data_cleansing import handle_missing_values

class TestMissingValues(unittest.TestCase):
    def test_handle_missing_age(self):
        """
        Test that missing 'age' values are handled correctly.
        """
        data = [{'name': 'Alice', 'age': '25'}, {'name': 'Bob', 'age': None}]
        cleaned_data = handle_missing_values(data)
        self.assertEqual(cleaned_data[1]['age'], '0')

if __name__ == '__main__':
    unittest.main()
