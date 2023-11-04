class Dog():
    species = 'mammal'
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name


    #OPERATIONS/Actions  ---> Methods
    def bark(self,number):
        print("Woof! My name is {} and the number is {}".format(self.name, number))


myDog = Dog('labra', 'Sammy')

myDog.bark(10) # Woof! My name is Sammy and the number is 10


class Circle():
    # Class object attribute
    pi = 3.14
    def __init__(self, radius=1):
        self.radius = radius

    #Method
    def get_circumference(self):
        return self.radius*self.pi * 2
    
my_circle = Circle()

c = my_circle.get_circumference()
print(c)#6.28
my_circle.radius = 10
c2 = my_circle.get_circumference()
print(c2) # 62.800000000000004

my_circle2 = Circle(30)
c3 = my_circle2.get_circumference()
print(c3) #188.4
    
