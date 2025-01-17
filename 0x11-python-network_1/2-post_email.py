#!/usr/bin/python3
"""
This script takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and displays the body of the response
(decoded in utf-8).
"""

import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode the email data into a query string
    data = urllib.parse.urlencode({"email": email}).encode("utf-8")

    # Send the POST request
    with urllib.request.urlopen(url, data) as response:
        body = response.read()

    # Decode the response body in utf-8
    print(body.decode("utf-8"))
