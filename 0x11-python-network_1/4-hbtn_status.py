#!/usr/bin/python3
"""
Fetches a URL using the requests package.
"""

import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    response_text = response.text

    print(
        f'Body response:\n\t- type: {type(response_text)}'
        f'\n\t- content: {response_text}'
    )
