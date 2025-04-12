import json
import os


def file_check():
    directory = "data"
    filename = "data.json"
    filepath = os.path.join(directory, filename)

    if not os.path.exists(directory):
        os.makedirs(directory)

    if not os.path.exists(filepath):
        initial_data = []

        with open(filepath, "w") as file:
            json.dump(initial_data, file, indent=4)
        print(f"File created with initial data at: {filepath}")
    else:
        print(f"File already exists at: {filepath}")

    with open(filepath, "r") as file:
        data = json.load(file)

    return data
