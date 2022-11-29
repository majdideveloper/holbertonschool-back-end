#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys
import json

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(api_url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(
        api_url + "todos", params={"userId": sys.argv[1]}).json()

    dicti = {str(user.get("id")): [{"task": task.get("title"),
                                    "completed": task.get("completed"),
                                    "username": user.get(
                                        "username")}for task in todos]}

    file_json = sys.argv[1] + ".json"
    with open(file_json, "w") as f:

        json.dump(dicti, f)
