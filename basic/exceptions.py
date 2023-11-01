# raise Exception("Error occured")

# raise FileExistsError("Missing")

# Handling Exception
try:
    a=9/0
except Exception as e:
    print(e) #division by zero

#Handling exception and Executing some statements irrespectivr of exception
finally:
    print("Always executes") #Always executes

