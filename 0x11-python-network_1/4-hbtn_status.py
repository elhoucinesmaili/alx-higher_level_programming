#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status
and displays the body of the response using the requests library.
"""

import requests

if __name__ == "__main__":
    # Fetch the URL
    response = requests.get("https://alx-intranet.hbtn.io/status")

    # Display the body of the response
    print("Body response:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t- content: {response.text}")
