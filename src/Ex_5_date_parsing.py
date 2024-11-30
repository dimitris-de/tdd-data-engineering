from datetime import datetime

def parse_date(date_str):
    """
    Parses a date string into a datetime object.

    Args:
        date_str (str): Date string.

    Returns:
        datetime: Parsed datetime object.

    Raises:
        ValueError: If the date format is not recognized.
    """
    formats = ['%Y-%m-%d', '%m/%d/%Y', '%B %d, %Y']
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    raise ValueError(f"Unsupported date format: {date_str}")
