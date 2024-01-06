#!/bin/bash
# Script that takes an URL and shows the Allowed OPTIONS
curl -s -I -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f2-