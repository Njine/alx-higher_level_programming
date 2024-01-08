#!/usr/bin/python3
"""
Sends a request to a specified URL and displays the response body.
Usage: ./check_http_status.py <URL>
  - Handles HTTP errors.
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
