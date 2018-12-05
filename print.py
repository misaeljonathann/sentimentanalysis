import json

obj = None
with open('data.json') as f:
    print(f)
    obj = json.load(f)
#print(json.dumps(parsed, indent=4, sort_keys=True))
outfile = open('file.json', 'w')
outfile.write(json.dumps(obj, indent=4, sort_keys=True))
outfile.close()

#print(json.dumps(json.dumps(obj)))