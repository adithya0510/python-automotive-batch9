from abc import ABC, abstractmethod
# Abstract class (cannot create object)
class Vehicle(ABC):
    # Abstract method (no implementation)
    @abstractmethod
    def start(self):
        pass
    # Concrete method (has implementation)
    def fuel_type(self):
        print("Vehicle uses fuel")

# Child class 1
class Car(Vehicle):
    # Implementation of abstract method
    def start(self):
        print("Car starts using a key")

# Child class 2
class Bike(Vehicle):

    # Implementation of abstract method
    def start(self):
        print("Bike starts using self-start button")

# Creating objects of child classes
car = Car()
bike = Bike()

# Calling abstracted behavior
car.start()
car.fuel_type()

bike.start()
bike.fuel_type()
