import json

with open('result.json') as json_data:
    d = json.load(json_data)
    print(d)
