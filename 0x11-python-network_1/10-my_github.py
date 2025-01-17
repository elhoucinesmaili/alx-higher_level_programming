#!/usr/bin/python3
"""
This script takes your GitHub credentials (username and personal access token)
and uses the GitHub API to display your GitHub user ID.
"""

import requests
import sys

if __name__ == "__main__":
    # Get GitHub credentials from command-line arguments
    username = sys.argv[1]
    token = sys.argv[2]

    # GitHub API URL for user information
    url = "https://api.github.com/user"

    # Use Basic Authentication with the username and token
    response = requests.get(url, auth=(username, token))

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response and display the user ID
        user_data = response.json()
        print(user_data.get("id"))
    else:
        # Print None if authentication fails or an error occurs
        print("None")
