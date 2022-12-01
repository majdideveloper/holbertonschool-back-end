#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""

import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in todos]}, jsonfile)
"""
import json
import requests
import sys


if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(api_url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(
        api_url + "todos", params={"userId": sys.argv[1]}).json()

    dicti = {user.get("id"): [{"task": task.get("title"),
                               "completed": task.get("completed"),
                               "username": user.get(
        "username")} for task in todos]}

    file_json = sys.argv[1] + ".json"
    with open(file_json, "w") as f:

        json.dump(dicti, f)"""
    
