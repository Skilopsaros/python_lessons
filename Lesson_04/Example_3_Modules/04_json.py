import json
import os

if os.path.isfile("my_json.json"):
    print("FILE FOUND")
    my_dict = json.load("my_json.json")
    print(my_dict)
else:
    print("FILE NOT FOUND")
    my_dict = {"name": "Ermis", "age": 25, "rating": "Awesome"}
    with open("my_json.json", "w") as file:
        file.write(json.dumps(my_dict, indent=2))
    print("json created")