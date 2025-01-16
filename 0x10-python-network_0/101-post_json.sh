#!/bin/bash
# Bash script sends a JSON POST request to URL as the 1st argument and displays the body of the response
curl -s -H "Content-Type: application/json" -d @"$2" "$1"
