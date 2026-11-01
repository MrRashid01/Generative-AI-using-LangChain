import json

with open("json_schema.json", "r") as file:
    schema = json.load(file)

print(schema)