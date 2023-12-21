import json

def update_config(file_path):
    # Open the file in read mode
    with open(file_path, 'r', encoding='utf-8') as json_file:
        # Load JSON data from the file
        employees_list = json.load(json_file)

    # Update the name of the second employee
    employees_list[1]['name'] = 'Bobby Deol'

    # Open the file in write mode and overwrite its content
    with open(file_path, 'w', encoding='utf-8') as json_file:
        # Write the modified list back to the file
        json.dump(employees_list, json_file)

    print('JSON file updated successfully')

# Specify the file path
file_path = 'employees.json'

# Call the update_config function
update_config(file_path)
