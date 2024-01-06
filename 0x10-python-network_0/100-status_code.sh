#!/bin/bash
# This script sends a request to the specified URL and displays only the status code of the response
curl -s -x -L HEAD -w "%{http_code}\n" "$1"
