#!/bin/bash
# This script sends a request to the specified URL and displays only the status code of the response
curl -s -X -L HEAD -w "%{http_code}" "$1"
