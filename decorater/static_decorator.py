# A static method in Python is a function defined within a class, marked with @staticmethod, which can be called without creating an instance of the class. It operates independently of instance or class-specific data, often used for utility functions within the class namespace.


# With static decorator
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# Calling the static method using the class
result_from_class = MathUtils.add(5, 3)
print(result_from_class)  # Output: 8

# Creating an instance of the class
math_utils_instance = MathUtils()

# Calling the static method using the instance
result_from_instance = math_utils_instance.add(10, 7)
print(result_from_instance)  # Output: 17



# Without Static Decorator
class MathUtils:
    def add(a, b):
        return a + b

# Calling the method using the class
result_from_class = MathUtils.add(5, 3)
print(result_from_class)  # Output: 8

# Creating an instance of the class
math_utils_instance = MathUtils()

# Calling the method using the instance (without @staticmethod, this would raise an error)
result_from_instance = math_utils_instance.add(10, 7)
print(result_from_instance)
