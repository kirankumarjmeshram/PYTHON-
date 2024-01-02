# Reverse arr
a = ['1','8','3','4',"6", "61"]
print(a[::-1]) # ['61', '6', '4', '3', '8', '1']

a = ['1','2','3','4',"6", "61"]
b = ['q','w','e','r','t','u']
for x, y in zip(a, b):
    print(x,y)
    # 1 q
    # 2 w
    # 3 e
    # 4 r
    # 6 t
    # 61 u

# Trick : Analyzing the most frequent on the list
a = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
print(max(set(a), key = a.count)) #4

# Trick : Reversing the string
a="python"
print("Reverse is", a[::-1]) # Reverse is nohtyp

# Splitting the string

a="Python is the language of the future"
b=a.split()
print(b) #['Python', 'is', 'the', 'language', 'of', 'the', 'future']

# Printing out multiple values of strings
print("on"*3+" " +"off"*2 +"*"*21) #ononon offoff*********************

#  Creating a single string

a = ["I", "am", "not", "available"]
print(" ".join(a)) #I am not available






