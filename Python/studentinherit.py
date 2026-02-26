class Student(Person):
    #pass

    def __init__(self,fname,lname):
    #add prop here
    #Person.__init__(self,fname,lname)
        super().__init__(fname,lname)
        self.gradyear = year

    def welcome(self):
        print("welcome")

x = Student("a","b",2025)
x.printname()