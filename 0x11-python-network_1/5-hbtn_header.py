#!/usr/bin/python3
"""
Fetches the X-Request-Id header variable of a request to a given URL.
Usage: ./get_request_id.py <URL>
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    request_id = response.headers.get("X-Request-Id")
    print(request_id)
