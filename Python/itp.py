class ITP(Person):
    #pass

    def __init__(self,fname,lname):
        #add prop here
        #Person.__init__(self,fname,lname)
        super().__init__(fname,lname)
        self.salary = salary

    def welcome(self):
        print("welcome")

x = Student("a","b",2025)
x.printname()