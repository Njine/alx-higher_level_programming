#!/usr/bin/python3
"""
Python script that retrieves GitHub user information using Basic Authentication
with a personal access token as the password.

Usage: ./10-my_github.py <username> <token>
  - The first argument is your GitHub username.
  - The second argument is your personal access token.

The script uses the requests package for HTTP communication.
"""

import sys
import requests

if __name__ == "__main__":
    url = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]

    auth = (username, password)
    response = requests.get(url, auth=auth)

    try:
        json_obj = response.json()
        print(json_obj.get("id"))
    except ValueError:
        print(None)
