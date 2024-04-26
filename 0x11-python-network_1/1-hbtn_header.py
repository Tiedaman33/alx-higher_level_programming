#!/usr/bin/python3
"""Sends a request to a URL and displays the
value of the X-Request-Id header."""

import urllib.request
import sys


def fetch_request_id(url):
    """Fetches the value of the X-Request-Id header from the given URL."""
    with urllib.request.urlopen(url) as response:
        request_id = response.getheader('X-Request-Id')
    return request_id


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-hbtn_header.py <URL>")
        sys.exit(1)
    url = sys.argv[1]
    request_id = fetch_request_id(url)
    print(request_id)
