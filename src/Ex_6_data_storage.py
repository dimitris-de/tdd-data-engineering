class DatabaseConnection:
    """
    Simulates a database connection.
    """
    def __init__(self):
        # Simulate connection setup
        pass

    def insert(self, data):
        """
        Inserts data into the database.

        Args:
            data (dict): Data to insert.

        Returns:
            bool: True if successful.
        """
        # Simulate data insertion
        return True

def save_to_db(data):
    """
    Saves data to the database.
    Args:
        data (dict): Data to save.
    Returns:
        bool: True if successful.
    """
    db = DatabaseConnection()
    return db.insert(data)
