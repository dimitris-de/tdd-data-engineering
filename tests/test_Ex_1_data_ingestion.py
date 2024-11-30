import unittest
from src.Ex_1_data_ingestion import parse_record, read_csv_file


class TestDataIngestion(unittest.TestCase):
    def test_read_csv_file(self):
        """
        Test that the read_csv_file function correctly reads a CSV file
        and returns the expected number of records.
        """
        data = read_csv_file('data/sample.csv')
        # Assuming sample.csv has 100 records
        self.assertEqual(len(data), 100)

    def test_read_csv_file_missing_fields(self):
        """
        Test reading a CSV file with missing fields.
        """
        data = read_csv_file('data/sample_missing_fields.csv')
        # Check that data is read without raising exceptions
        self.assertGreater(len(data), 0)

    def test_read_csv_file_additional_fields(self):
        """
        Test reading a CSV file with additional fields.
        """
        data = read_csv_file('data/sample_additional_fields.csv')
        # Verify that additional fields are included
        self.assertIn('extra_field', data[0])

    def test_parse_old_schema(self):
        """
        Test parsing of records with the old schema.
        """
        record = {'name': 'Alice', 'age': '30'}
        parsed = parse_record(record)
        self.assertEqual(parsed['email'], '')

    def test_parse_new_schema(self):
        """
        Test parsing of records with the new schema.
        """
        record = {'name': 'Bob', 'age': '25', 'email': 'bob@example.com'}
        parsed = parse_record(record)
        self.assertEqual(parsed['email'], 'bob@example.com')


if __name__ == '__main__':
    unittest.main()
