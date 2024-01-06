#!/bin/bash
# This script sends a POST request and displays the response body
curl -s "$1" -X POST --data-urlencode "email=test@gmail.com" --data-urlencode "subject=I will always be here for PLD"
