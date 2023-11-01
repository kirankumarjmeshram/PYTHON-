# Unpack Operators (*args & **kwargs): Unpack operators separates a collection of elements 
# from a list or tuple into individual elements. 
# *args for positional and **kwargs for keyward arguments.Usually used to unpack and pass as arguments to a function.
# Single asterisk (*) is for Lists/Tuples and double asterisk (**) is for dictionaries.

x = [1,2,3,4,5]

print(x) #[1, 2, 3, 4, 5]

print(*x) #1 2 3 4 5

def func(*args, **kwargs):
    print(args, kwargs)
    print(*args)
    print(*kwargs)
#printouts the touple with positional args and dict with kwargs
func(1,2,3,4,a=11,b=22)
#(1, 2, 3, 4) {'a': 11, 'b': 22}
#1 2 3 4
#a b

def func(a,b):
    print(a,b)

#passing a list of tuples to the function
groups = [(1,2), (3,4)]

for group in groups:
    func(*group)
    # 1 2
    # 3 4

#passing a Dictonary to the function
dict = {'a':5, 'b':6}

func(**dict)
#5 6