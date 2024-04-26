#!/usr/bin/python3
"""Sends a POST request to a URL with an email
as a parameter and displays the body of the response."""

import urllib.request
import urllib.parse
import sys


def post_email(url, email):
    """Sends a POST request with the email parameter to the given URL."""
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')
    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
    return body


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./2-post_email.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]
    response_body = post_email(url, email)
    print(response_body)
