#!/usr/bin/python3
"""
Python script to send a POST request to http://0.0.0.0:5000/search_user
with a letter as a parameter and handle the response.
"""
import sys
import requests

def main():
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    payload = {'q': letter}
    url = "http://0.0.0.0:5000/search_user"

    try:
        response = requests.post(url, data=payload)
        response_json = response.json()
        
        if response_json:
            print("[{}] {}".format(response_json.get("id"), response_json.get("name")))
        else:
            print("No result")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
    except ValueError:
        print("Not a valid JSON")

if __name__ == "__main__":
    main()

