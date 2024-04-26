#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status and displays the body of the response."""

import urllib.request

def fetch_status():
    """Fetches the status from the given URL."""
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        body = response.read()
        utf8_content = body.decode('utf-8')
    return body, utf8_content

if __name__ == "__main__":
    body, utf8_content = fetch_status()
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(utf8_content))

