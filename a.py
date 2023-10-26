# a = 20
# b=a
# print(id(a), id(b))

dict = {'1':'Mumbai', '2':'Pune', '3':'Nagpur'}

for key in dict:
    print(dict[key])

for key, value in dict.items():
    print(key, value)

for key in dict.keys():
    print (key)