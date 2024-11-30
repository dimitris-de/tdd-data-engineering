def normalize_column(data):
    """
    Normalizes a list of numerical values using Min-Max scaling.

    Args:
        data (list): List of numerical values.

    Returns:
        list: Normalized list of values between 0 and 1.
    """
    if not data:
        return []
    min_val = min(data)
    max_val = max(data)
    range_val = max_val - min_val
    if range_val == 0:
        # All values are the same
        return [0.0 for _ in data]
    normalized_data = [(x - min_val) / range_val for x in data]
    return normalized_data

def calculate_sum(data):
    """
    Calculates the sum of a list of numbers.

    Args:
        data (list): List of numerical values.

    Returns:
        float: The sum of the values.
    """
    return sum(data)

def calculate_mean(data):
    """
    Calculates the mean of a list of numbers.

    Args:
        data (list): List of numerical values.

    Returns:
        float: The mean value.
    """
    if not data:
        return 0.0
    return sum(data) / len(data)
