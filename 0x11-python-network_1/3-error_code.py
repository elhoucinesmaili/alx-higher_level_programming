#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL, and displays the body
of the response (decoded in utf-8). If an HTTPError occurs, it prints the error
code instead of the response body.
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        # Send the request
        with urllib.request.urlopen(url) as response:
            body = response.read()

        # Decode and print the response body
        print(body.decode("utf-8"))
    except urllib.error.HTTPError as e:
        # Print the error code in case of an HTTPError
        print(f"Error code: {e.code}")
