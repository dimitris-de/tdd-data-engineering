def process_data(api_client, db_client):
    """
    Processes data using injected API and database clients.

    Args:
        api_client (object): API client with a fetch method.
        db_client (object): Database client with a save method.
    """
    data = api_client.fetch()
    db_client.save(data)
