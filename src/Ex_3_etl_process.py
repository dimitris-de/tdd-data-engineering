import csv
from src.Ex_1_data_ingestion import read_csv_file
from src.Ex_2_data_transformation import normalize_column

def extract_data(file_path):
    """
    Extracts data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        list: List of records.
    """
    return read_csv_file(file_path)

def validate_data(record):
    """
    Validates a single data record.

    Args:
        record (dict): Data record.

    Raises:
        ValueError: If 'age' is not a number.
        KeyError: If 'name' or 'age' is missing.
    """
    # Ensure 'name' and 'age' keys are present
    if 'name' not in record or 'age' not in record:
        raise KeyError("Missing 'name' or 'age' in record.")

    # Validate 'age' is a number
    try:
        age = int(record['age'])
        if age < 0:
            raise ValueError("'age' must be non-negative.")
    except ValueError:
        raise ValueError("'age' must be a valid integer.")

    # If all validations pass
    return True

def transform_data(data):
    """
    Transforms data by normalizing the 'value' column.

    Args:
        data (list): List of records.

    Returns:
        list: Transformed data.
    """
    values = [float(record['value']) for record in data]
    normalized_values = normalize_column(values)
    for i, record in enumerate(data):
        record['normalized_value'] = normalized_values[i]
    return data

def load_data(data, file_path):
    """
    Loads data into a CSV file.

    Args:
        data (list): List of records.
        file_path (str): Output file path.

    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        with open(file_path, mode='w', newline='', encoding='utf-8') as csvfile:
            fieldnames = data[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
