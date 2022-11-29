#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(api_url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(
        api_url + "todos", params={"userId": sys.argv[1]}).json()

    nameFile = eval(sys.argv[1]) + ".csv"

    f = open(nameFile, "x")
    f.write([print("{},{},{},{}".format(str(user.get("id")), str(
        user.get("username")), str(task.get("completed")), str(task.get("title")))) for task in todos ])
