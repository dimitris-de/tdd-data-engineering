import aiohttp

async def fetch_data_async(url):
    """
    Asynchronously fetches data from a URL.

    Args:
        url (str): URL to fetch data from.

    Returns:
        dict: JSON data.
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data
