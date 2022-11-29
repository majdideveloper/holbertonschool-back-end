#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys
import json

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(api_url + "users/{}".format(sys.argv[1])).json()
    print(user)
    todos = requests.get(
        api_url + "todos", params={"userId": sys.argv[1]}).json()