#!/usr/bin/python3
"""
Sends request to a given URL; displays response body.
Usage: ./3-error_code.py <URL>
  - Handles urllib.error.HTTPError exceptions; prints the HTTP status code.
"""

import sys
import urllib.error
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
