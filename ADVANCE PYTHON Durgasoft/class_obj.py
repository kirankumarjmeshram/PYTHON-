class student:
    def __init__(self, roll, name):
        self.name = name
        self.roll = roll

    def talk(self):
        print(f"my name is {self.name}")
        print(f"my roll num is {self.roll}")
        
s = student(12, "Abhishek")

print(s.name) #Abhishek

print(s.talk())
# my name is Abhishek
# my roll num is 12

s.name = "Raghav"
print(s.name) #Raghav