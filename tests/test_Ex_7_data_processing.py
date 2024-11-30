import unittest
from unittest.mock import MagicMock
from src.Ex_7_data_processing import process_data


class TestDataProcessing(unittest.TestCase):
    def test_process_data(self):
        """
        Test process_data function with mocked dependencies.
        """
        # Mock API client
        mock_api_client = MagicMock()
        mock_api_client.fetch.return_value = {'key': 'value'}

        # Mock DB client
        mock_db_client = MagicMock()
        mock_db_client.save.return_value = True

        # Call the function
        process_data(mock_api_client, mock_db_client)

        # Assertions
        mock_api_client.fetch.assert_called_once()
        mock_db_client.save.assert_called_once_with({'key': 'value'})

if __name__ == '__main__':
    unittest.main()
