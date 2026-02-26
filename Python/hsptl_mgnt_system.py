class Staff:  #given base class as staff
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary
    
    def duties(self):
        return "Hospital Duties"
    
    def cal_salary(self):
        return self.base_salary
    
# Receptionist class
class Receptionist(Staff):
    def duties(self):
        return f"{self.name} is Responsible for Maintainance of the Hospital"
    
    def cal_salary(self):
        return self.base_salary + 10000
    
# Nurse class
class Nurse(Staff):
    def duties(self):
        return f"{self.name} helps and assists Doctors when needed"
    
    def cal_salary(self):
        return self.base_salary + 15000
    
# Doctor class
class Doctor(Staff):
    def duties(self):
        return f"{self.name} does operations and surgeries"
    
    def cal_salary(self):
        return self.base_salary + 20000


def generate_report(staff):
    print("Name:", staff.name)
    print("Duties:", staff.duties())
    print("Salary:", staff.cal_salary())


d1 = Doctor("Dr.Ramesh", 50000)
n1 = Nurse("Anjali", 30000)
r1 = Receptionist("Kiran", 20000)

generate_report(d1)
generate_report(n1)
generate_report(r1)
