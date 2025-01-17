#!/usr/bin/python3
"""
This script takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response.
"""

import requests
import sys

if __name__ == "__main__":
    # Get the URL and email from command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Create a dictionary for the POST data
    data = {'email': email}

    # Send the POST request
    response = requests.post(url, data=data)

    # Display the body of the response
    print(response.text)
