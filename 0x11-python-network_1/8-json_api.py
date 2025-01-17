#!/usr/bin/python3
"""
This script takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.

The response is parsed as JSON and handled accordingly.
"""

import requests
import sys

if __name__ == "__main__":
    # Get the letter from the command line argument
    # If no argument is given, set q to an empty string
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    # Prepare the POST request payload
    payload = {'q': q}

    try:
        # Send the POST request
        response = requests.post("http://0.0.0.0:5000/search_user", data=payload)
        
        # Try to parse the response as JSON
        json_data = response.json()

        # Check if the JSON is empty
        if json_data:
            print(f"[{json_data.get('id')}] {json_data.get('name')}")
        else:
            print("No result")
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")
