import json

obj = None
with open('data.json') as f:
    obj = json.load(f)
    print(obj["created_at"])
#print(json.dumps(parsed, indent=4, sort_keys=True))
outfile = open('file.json', 'w')
outfile.write(json.dumps(obj, indent=4, sort_keys=True))
outfile.close()

#print(json.dumps(json.dumps(obj)))