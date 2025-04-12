import json
import os

directory = "data"
filename = "data.json"
filepath = os.path.join(directory, filename)

with open(filepath, "r") as file:
    data = json.load(file)


def create():
    todo = input("What is your task? ")
    priority = 5
    priority = input("What's its priority (default is 5/10) ")

    data.append({"name": todo, "rank": priority})

    with open(filepath, "w") as file:
        json.dump(data, file, indent=4)


# def status():

