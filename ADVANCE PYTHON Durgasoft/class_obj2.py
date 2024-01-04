# constructor overloading or method overloding is not applicable in python
# only latest one constructor willl woek
class Test:
    # not work
    def __init__(self, x): 
        print("one arg")

    # work
    def __init__(self):
        print("no arg")

    
t1 = Test() #no arg
t2 = Test() # no arg


class Test2:
    def __init__(self):
        print("no arg")

    def __init__(self, x):
        print("one arg")

    
    
t1 = Test2(1) #one arg
t2 = Test2(2) #one arg