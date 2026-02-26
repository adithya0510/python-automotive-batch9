class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

        def move(self):
            print("drive")


class Boat:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

        def move(self):
            print("sail")

class Truck:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

        def move(self):
            print("turn with more mileage")

car = Car("ford","figo")
boat = Boat("Ibizza","I20")
truck = Truck("Mahindra","t20")

for x in (car,boat,truck):
    print(x.move())