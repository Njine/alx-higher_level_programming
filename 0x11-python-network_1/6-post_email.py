#!/usr/bin/python3
"""
Sends a POST request to a specified URL with a given email.
Usage: ./post_email_requests.py <URL> <email>
  - Displays the body of the response.
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email_value = {"email": sys.argv[2]}
    response = requests.post(url, data=email_value)
    print(response.text)
