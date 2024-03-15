"""Tests standard tap features using the built-in SDK tests library."""

import datetime

from singer_sdk.testing import get_standard_tap_tests

from tap_vitallyapi.tap import Tapvitallyapi

SAMPLE_CONFIG = {
"api_key": "Basic c2tfbGl2ZV9jMzY3MjJjNDNmZDk4OWQ0YjhiMzE1MTg0MThiMDA4YjAzZTZlN2M2MTAzM2Q4MjM4NDc5MjRmNDUwMDJlMzhlOg==" 
    
    # TODO: Initialize minimal tap config
}


# Run standard built-in tap tests from the SDK:
def test_standard_tap_tests():
    """Run standard tap tests from the SDK."""
    tests = get_standard_tap_tests(
        Tapvitallyapi,
        config=SAMPLE_CONFIG
    )
    
    for test in tests:
        test()


# TODO: Create additional tests as appropriate for your tap.
