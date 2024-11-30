import unittest
from src.Ex_5_date_parsing import parse_date

class TestDateParsing(unittest.TestCase):
    def test_parse_iso_format(self):
        """
        Test parsing of ISO date format.
        """
        date_str = '2021-10-15'
        date_obj = parse_date(date_str)
        self.assertEqual(date_obj.year, 2021)

    def test_parse_us_format(self):
        """
        Test parsing of US date format.
        """
        date_str = '10/15/2021'
        date_obj = parse_date(date_str)
        self.assertEqual(date_obj.month, 10)

    def test_parse_invalid_format(self):
        """
        Test that invalid date formats raise ValueError.
        """
        date_str = '15-10-2021'
        with self.assertRaises(ValueError):
            parse_date(date_str)

if __name__ == '__main__':
    unittest.main()
