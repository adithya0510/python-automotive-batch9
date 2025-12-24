class Teacher(Person):
    #pass

    def __init__(self,fname,lname,tid):
        #add prop here
        #Person.__init__(self,fname,lname)
        super().__init__(fname,lname)
        self.id = tid

    def welcome(self):
        print("welcome")

x = Student("a","b",10)
x.printname()