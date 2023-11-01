# Comprehensions : Comprehensions are not found in other programming 
#languages. It provides us with a short and concise way to construct new sequences (such as lists, set, dictionary etc.).

x = [i + 5 for i in range(10)] 
print(x) # [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

#get increment for 5
y = [i for i in range(100) if i%5 ==0]
print(y) #[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

z = {i for i in range(100) if i%5 == 0}
print(z) # [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]