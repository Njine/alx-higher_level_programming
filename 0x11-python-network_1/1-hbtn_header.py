#!/usr/bin/python3
"""
Fetches the X-Request-Id variable value from the header
of a response to a given URL.
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        x_request_id = dict(response.headers).get("X-Request-Id")
        print(x_request_id)
