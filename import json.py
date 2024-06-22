import json

# Sample JSON data
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Convert the data to a JSON formatted string with 4 spaces of indentation
json_str = json.dumps(data, indent=4)

# Print the pretty-printed JSON string
print(json_str)