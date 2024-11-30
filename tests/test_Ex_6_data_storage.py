import unittest
from unittest.mock import patch, MagicMock

from src.Ex_6_data_storage import save_to_db


class TestDataStorage(unittest.TestCase):
    @patch('src.Ex_6_data_storage.DatabaseConnection')
    def test_save_to_db(self, mock_db_conn):
        """
        Test save_to_db function with a mocked database connection.
        """
        # Create a mock instance
        mock_instance = MagicMock()
        mock_instance.insert.return_value = True
        mock_db_conn.return_value = mock_instance

        # Call the function
        result = save_to_db({'data': 'test'})

        # Assertions
        mock_instance.insert.assert_called_once_with({'data': 'test'})
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
