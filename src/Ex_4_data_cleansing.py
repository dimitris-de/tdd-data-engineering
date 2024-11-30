def handle_missing_values(data):
    """
    Handles missing 'age' values by imputing a default value.

    Args:
        data (list): List of records.

    Returns:
        list: Data with missing values handled.
    """
    for record in data:
        if not record.get('age'):
            record['age'] = '0'  # Default value
    return data
