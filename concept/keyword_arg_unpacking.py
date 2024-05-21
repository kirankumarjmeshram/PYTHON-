# When used in the context of function arguments, ** is used to unpack a dictionary into keyword arguments. 
# This allows you to pass multiple keyword arguments to a function dynamically.

def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

# Using a dictionary to store arguments
person_info = {'name': 'Alice', 'age': 30}

# Unpacking the dictionary into keyword arguments
greet(**person_info)
