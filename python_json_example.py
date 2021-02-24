import json

with open('read_file.json', 'r') as fh:
	json_str = fh.read()
	json_value = json.loads(json_str)
	print(type(json_value))
	print(json_value['name'])


# print(json.dumps(a, indent=2))

# print(json.dumps(a, indent=2, separators=('. ', ' = ')))
# print(json.dumps(a, indent=2, sort_keys=True))
