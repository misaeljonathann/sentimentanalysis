import json

#Store JSON data into json_file
with open("example.json") as json_file:
    json_data = json.loads(json_file)
    print(json_data)