import unittest
from unittest.mock import patch, MagicMock
from src.Ex_10_data_pipeline import extract_data, load_data, transform_data


class TestDataPipeline(unittest.TestCase):
    @patch('src.Ex_10_data_pipeline.requests.get')
    def test_extract_data(self, mock_get):
        """
        Test data extraction from API.
        """
        mock_response = MagicMock()
        mock_response.json.return_value = {'results': [{'value': 1}]}
        mock_get.return_value = mock_response

        data = extract_data('http://api.example.com/data')
        self.assertEqual(data, [{'value': 1}])

    def test_transform_data(self):
        """
        Test data transformation logic.
        """
        data = [{'value': 1}, {'value': 2}]
        transformed = transform_data(data)
        self.assertEqual(transformed, [{'value': 1, 'value_squared': 1}, {'value': 2, 'value_squared': 4}])

    @patch('src.Ex_10_data_pipeline.DatabaseClient')
    def test_load_data(self, mock_db_client_class):
        """
        Test data loading into the database.
        """
        mock_db_client = MagicMock()
        mock_db_client_class.return_value = mock_db_client

        data = [{'value': 1, 'value_squared': 1}]
        result = load_data(data)
        mock_db_client.insert_many.assert_called_once_with(data)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
