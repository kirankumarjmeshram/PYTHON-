#Python's pass by assignment is and additionally shows the difference between pass by value and pass by reference
#Python functions handle primitive and non-primitive data types
def func(x,y):
    x=x-1
    y.pop()

if __name__ == "__main__":
    i=10
    j=['a','b','c']

    func(i,j.copy()) # here i & j passed by value

    print(i,j) #10 ['a', 'b', 'c']

    func(i,j) #j is passed by ref

    print(i,j) #10 ['a', 'b'] 

    k=j
    l=j.copy()
    print(id(j)) #1648050147712
    print(id(k)) #1648050147712
    print(id(l)) #1648054533760