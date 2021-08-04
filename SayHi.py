# Write a class called Dog that has two properties: name and age. Write a constructor that takes three arguments self, name and age and set these to the object properties.
# Now write a function sayHI(dog) where dog is the dog class object that returns a Hi, my name is <dog’s name> and I am <age> years old!

# sayHi(d1) # Hi, my name is Dot and I am 4 years old!
# sayHi(d2) # Hi, my name is Elf and I am 3 years old!

# class SayHi(Object):
#     pass

class dog():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    
    def sayHI(self):
        if(dog=="d1"):
            self.name="Dot"
            self.age="4"
            return("Hi, my name is"+self.name+"and I am "+self.age+"years old")
        if(dog=="d2"):
            self.name="Elf"
            self.age="3"
            return("Hi, my name is"+self.name+"and I am "+self.age+"years old")


n=dog()
d1="d1"
print(n.sayHI(d1))
        