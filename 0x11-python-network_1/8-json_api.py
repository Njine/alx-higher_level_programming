#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user
with a specified letter.
Usage: ./search_user_requests.py <letter>
  - The variable `q` is assigned the value of the provided letter.
  - If no letter is provided, the script sends `q=""`.
"""

import sys
import requests

if __name__ == "__main__":
    input_letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": input_letter}
    response = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        parsed_response = response.json()
        if parsed_response == {}:
            print("No result")
        else:
            print("[{}] {}".format(
                parsed_response.get("id"), parsed_response.get("name")
            ))
    except ValueError:
        print("Not a valid JSON")
