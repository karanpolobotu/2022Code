# class Inheritance, fare charge is 10% more than total fare if bus

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def aFare(self):
        return Bus.fare(self) * 1.1

School_bus = Bus("School Volvo", 12, 50)

# change the fare in a new method by calling the bus fare

print("Total Bus fare is:", School_bus.aFare())
