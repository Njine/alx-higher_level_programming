#!/bin/bash
# This script retrieves the Content-Length from an HTTP request
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2
