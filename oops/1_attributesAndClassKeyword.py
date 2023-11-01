class Dog():
     
    def __init__(self, breed, name, spots):
        #Attribute
        #We take in the argument
        #Assign it using self.attribute_name(=breed)
        self.breed = breed
        self.name = name

        # Expect boolean True/False
        self.spots = spots

myDog = Dog(breed='labra', name='Sammy', spots=False)

print(type(myDog)) #__main__.Dog
print(myDog.breed) #labra
print(myDog.name)  #Sammy
print(myDog.spots) #False