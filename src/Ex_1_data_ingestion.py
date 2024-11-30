import csv

def read_csv_file(file_path):
    """
    Reads a CSV file and returns a list of records.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        list: A list of dictionaries representing the CSV records.
    """
    data = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return data


def parse_record(record):
    """
    Parses a record, accommodating schema changes.

    Args:
        record (dict): Data record.

    Returns:
        dict: Parsed record with standardized fields.
    """
    parsed = {
        'name': record.get('name', ''),
        'age': record.get('age', '0'),
        'email': record.get('email', '')
    }
    return parsed
