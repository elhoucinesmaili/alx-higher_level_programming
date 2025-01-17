#!/usr/bin/python3
"""
This script takes a repository name and an owner name as arguments
and uses the GitHub API to display the 10 most recent commits.
"""

import requests
import sys

if __name__ == "__main__":
    # Get repository name and owner name from command-line arguments
    repo = sys.argv[1]
    owner = sys.argv[2]

    # GitHub API URL for listing commits
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    # Send a GET request to fetch the commits
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        commits = response.json()

        # Display the 10 most recent commits
        for commit in commits[:10]:
            sha = commit.get("sha")
            author = commit.get("commit", {}).get("author", {}).get("name")
            print(f"{sha}: {author}")
    else:
        print(f"Error: Unable to fetch commits (HTTP {response.status_code})")
