import json

file_path = 'employees.json'

# Check if the file exists
try:
    with open(file_path, 'r', encoding='utf-8') as json_file:
        employees_list = json.load(json_file)

    # Update the name of the second employee
    employees_list[1]['name'] = 'Bobby Deol'

    # Open the file in write mode and overwrite its content
    with open(file_path, 'w', encoding='utf-8') as json_file:
        # Write the modified list back to the file
        json.dump(employees_list, json_file)

    print('JSON file updated successfully')
except FileNotFoundError:
    print(f"The file '{file_path}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
