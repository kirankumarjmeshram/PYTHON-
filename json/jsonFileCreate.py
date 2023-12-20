import json

data = {}

data['key'] = 'value'

# Convert the dictionary to JSON data

json_data = json.dumps(data)
i = 0
file_path = f"/home/sarutobi/Documents/GitHub/PYTHON/json/generated_json_files/output{i}.json"
# create only one
# with open(file_path, 'w') as json_file:
#     json_file.write(json_data)

for i in range(10):
    with open(f"/home/sarutobi/Documents/GitHub/PYTHON/json/json_files/output{i}.json", 'w') as json_file:
        json_file.write(json_data)
