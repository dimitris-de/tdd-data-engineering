# tests/test_Ex_8_data_fetching.py

import unittest
from aiohttp import web, ClientResponseError
from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop

from src.Ex_8_data_fetching import fetch_data_async

"""
Unit Tests for the `fetch_data_async` Function

This module tests the behavior of the `fetch_data_async` function, which performs asynchronous HTTP requests.
The tests are written using the `unittest` framework in conjunction with `aiohttp`'s test utilities to
simulate a web server for realistic testing scenarios.

Key Components:
1. `AioHTTPTestCase`:
   - Base class provided by `aiohttp.test_utils` for creating test cases with an embedded web server.
   - Allows the definition of routes and handlers to simulate server responses.

2. `mock_handler_success`:
   - A mock route handler that simulates a successful server response.
   - Returns a JSON payload: `{'data': 'expected'}`.

3. `mock_handler_failure`:
   - A mock route handler that simulates a server error by raising an `HTTPInternalServerError`.

4. `fetch_data_async`:
   - The function being tested.
   - Assumes this function makes an asynchronous HTTP request and handles responses or errors.

Test Cases:
1. `test_fetch_data_async_success`:
   - Tests the successful behavior of `fetch_data_async` when the server responds with a valid JSON payload.
   - The `mock_handler_success` is used to return the expected response.
   - Verifies that the result matches the expected data.

2. `test_fetch_data_async_failure`:
   - Tests how `fetch_data_async` handles an HTTP error response.
   - The `mock_handler_failure` is used to simulate an error.
   - Verifies that the function raises a `ClientResponseError` and checks that its status is `500`.

How It Works:
1. `get_application`:
   - Sets up a test `aiohttp` application with two routes (`/data` and `/error`).
   - Each route is assigned a corresponding mock handler.

2. Test Flow:
   - The test server is initialized by `AioHTTPTestCase`.
   - `fetch_data_async` is called with URLs generated using `self.server.make_url`.
   - Assertions are used to validate function behavior under success and failure scenarios.

Dependencies:
1. `aiohttp`:
   - Required for `web.Application`, `web.json_response`, and `ClientResponseError`.

Considerations for Further Testing:
1. Edge cases such as:
   - Network timeouts.
   - Invalid or malformed URLs.
   - Non-JSON or unexpected payload formats.
2. For modern Python versions (3.8+), consider using `pytest` with `pytest-asyncio` for improved async testing support.

Usage:
- This test suite can be executed by running the module directly:
    `python tests/test_Ex_8_data_fetching.py`

"""


class TestAsyncFetch(AioHTTPTestCase):
    async def get_application(self):
        app = web.Application()
        app.router.add_get('/data', self.mock_handler_success)
        app.router.add_get('/error', self.mock_handler_failure)
        return app

    async def mock_handler_success(self, request):
        return web.json_response({'data': 'expected'})

    async def mock_handler_failure(self, request):
        raise web.HTTPInternalServerError()

    @unittest_run_loop
    async def test_fetch_data_async_success(self):
        url = self.server.make_url('/data')
        result = await fetch_data_async(url)
        self.assertEqual(result, {'data': 'expected'})

    @unittest_run_loop
    async def test_fetch_data_async_failure(self):
        url = self.server.make_url('/error')
        with self.assertRaises(ClientResponseError) as context:
            await fetch_data_async(url)
        self.assertEqual(context.exception.status, 500)

if __name__ == '__main__':
    unittest.main()
