# To work with JSON files in Python, you use the built-in json module. This module allows you to read and write JSON data. Below is a detailed guide on how to use it.

# 1. Reading JSON data from a file

# To read and convert JSON into a Python data structure (like a dictionary or list), you use the json.load() function.

# Example:

# Suppose you have a JSON file called data.json with the following content:

# {
#     "name": "Hasan",
#     "age": 25,
#     "isStudent": true,
#     "courses": ["Math", "Physics", "Chemistry"],
#     "address": {
#         "city": "Tabriz",
#         "postalCode": "12345"
#     }
# }

# To read this file:

# import json

# # Open and read the JSON file
# with open('data.json', 'r') as file:
#     data = json.load(file)

# # Accessing the data
# print(data['name'])        # Hasan
# print(data['address']['city'])  # Tabriz

# 2. Writing data to a JSON file

# To store a Python dictionary or list into a JSON file, you use the json.dump() function.

# Example:

# import json

# # Data in the form of a Python dictionary
# data = {
#     "name": "Hasan",
#     "age": 25,
#     "isStudent": True,
#     "courses": ["Math", "Physics", "Chemistry"],
#     "address": {
#         "city": "Tabriz",
#         "postalCode": "12345"
#     }
# }

# # Open and write the data to a JSON file
# with open('data.json', 'w') as file:
#     json.dump(data, file, indent=4)  # indent makes the output formatted nicely

# 3. Converting JSON to a string and vice versa

# If you want to work with JSON as a string in Python (instead of a file), you can use json.dumps() to convert a Python dictionary to a JSON string, and json.loads() to convert a JSON string back into a dictionary.

# Converting a dictionary to a JSON string:

# import json

# data = {
#     "name": "Hasan",
#     "age": 25,
#     "isStudent": True
# }

# json_string = json.dumps(data, indent=4)
# print(json_string)

# Converting a JSON string to a dictionary:

# import json

# json_string = '{"name": "Hasan", "age": 25, "isStudent": true}'

# data = json.loads(json_string)
# print(data['name'])  # Hasan

# Key functions:

# json.load(): Reads JSON data from a file.

# json.dump(): Writes Python data to a JSON file.

# json.loads(): Converts a JSON string into a Python dictionary.

# json.dumps(): Converts a Python dictionary into a JSON string.


# These functions allow you to easily convert data between JSON and Python and use them in your programs.