#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import sys
import requests

if __name__ == "__main__":
    # Assign the letter from the arguments or use an empty string if no argument is given
    letter = sys.argv[1] if len(sys.argv) > 1 else ""

    # Define the URL and send the POST request with the 'q' parameter
    url = "http://0.0.0.0:5000/search_user"
    data = {"q": letter}
    response = requests.post(url, data=data)

    try:
        # Attempt to parse the response as JSON
        json_data = response.json()

        # Check if the JSON is empty
        if not json_data:
            print("No result")
        else:
            # Print the ID and name from the JSON response
            print(f"[{json_data.get('id')}] {json_data.get('name')}")
    except requests.exceptions.JSONDecodeError:
        # Handle invalid JSON responses
        print("Not a valid JSON")
