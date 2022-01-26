#create bus class that inherits from vehicle class, but give Bus.seating_capacity() a default value of 50

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):

    #use method overriding to create new method with default capacity
    def seating_capacity(self, capacity = 50):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

newBus = Bus("new bus", 100, 6)

oldBus = Bus("old bus", 100, 10)

print(newBus.seating_capacity())

print(newBus.seating_capacity(100))
