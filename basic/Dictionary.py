# Strings, numbers, tuples as dict keys
# dict fns
    # str(dict) 
    # len(dict)
    # type (variable)

dict = {'1':'Mumbai', '2':'Pune', '3':'Nagpur'}
print(len(dict))
print(str(dict)) # gives in string format
print(type(dict)) #<class 'dict'>

# Dictonary METHODS
    # dict.clear()
    # dict.copy()
    # dict.fromkeys()
    # dict.get(key, default=None)
    # dict.has(key)
    # dict.items()
    # dict.keys()
    # dict.setdefault(key, defaulf=None)
    # dict.update((dict2))
    
for key, value in dict.items():
    print(key,value)
    # 1 Mumbai
    # 2 Pune
    # 3 Nagpur

for a, b in dict.items():
    print(a,b)
    # 1 Mumbai
    # 2 Pune
    # 3 Nagpur
