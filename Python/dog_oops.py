class Dog:
    #first define the common and then the unique
    #can be called a constructor
    def __init__(self,name,age):
        self.name = name   #lucy name
        self.age = age     #4yrs age

    def bark(self): 
        # attributes unique to each instance of Dog class
        return f"{self.name} deosn't bark!"

dog1 = Dog("Lucy",4)
dog2 = Dog("test",3)
# can create as many number of dogs as per the requirement

print(dog1.bark())
print(dog2.bark())