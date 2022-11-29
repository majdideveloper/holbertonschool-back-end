#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import json
import requests
import sys


if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    
    users = requests.get(api_url + "users")
   
    
    for user in users:
        todos = requests.get(
        api_url + "todos", params={"userId": user.get("id")}).json()
        dicti = {user.get("id"): [{"task": task.get("title"),
                               "completed": task.get("completed"),
                               "username": user.get(
        "username")} for task in todos]}

    file_json = sys.argv[1] + ".json"
    with open(file_json, "w") as f:
        json.dump(dicti, f)
