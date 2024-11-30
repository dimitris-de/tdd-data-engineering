import requests

def extract_data(api_url):
    """
    Extracts data from an API.

    Args:
        api_url (str): API endpoint.

    Returns:
        list: Extracted data.
    """
    response = requests.get(api_url)
    response.raise_for_status()
    return response.json()['results']

def transform_data(data):
    """
    Transforms data by adding a 'value_squared' field.

    Args:
        data (list): List of records.

    Returns:
        list: Transformed data.
    """
    for record in data:
        record['value_squared'] = record['value'] ** 2
    return data

class DatabaseClient:
    """
    Simulates a database client.
    """
    def insert_many(self, data):
        """
        Inserts multiple records into the database.

        Args:
            data (list): Data to insert.
        """
        # Simulate insertion
        pass

def load_data(data):
    """
    Loads data into the database.

    Args:
        data (list): Data to load.

    Returns:
        bool: True if successful.
    """
    db_client = DatabaseClient()
    try:
        db_client.insert_many(data)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def run_pipeline(api_url):
    """
    Runs the full data pipeline.

    Args:
        api_url (str): API endpoint.
    """
    data = extract_data(api_url)
    data = transform_data(data)
    success = load_data(data)
    if success:
        print("Pipeline executed successfully.")
    else:
        print("Pipeline execution failed.")
