#!/bin/bash
# This script sends a JSON POST request to the specified URL and displays the response body
curl -s "$1" -X POST -H "Content-Type: application/json" -d "@$2"
