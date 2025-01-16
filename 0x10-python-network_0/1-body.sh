#!/bin/bash
# Script that takes in a URL, sends a GET request, and displays the body of a 200 status code response
curl -s -L -X GET "$1" -o - -w "%{http_code}" | awk '{if ($NF == "200") {sub($NF,""); print}}'
