a = [1,2,3,4,5]

b = map(lambda i : i*2, a)
print(list(b)) #[2, 4, 6, 8, 10]

c = filter(lambda i: i>2,a)
print(list(c)) #[3, 4, 5]

def fun(x):
    return x%2==0

d = filter(fun,a)
print(list(d)) #[2, 4]