#create a child class Bus that will inherit all of the variables and methods of the Vehicle class

class Vehicle:
#created vehicle class

    def __init__(self, name, max_speed, mileage):
        #defined constructor and instance variables
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


#created child class. If child class inherits nothing new, leave empty with pass
class Bus(Vehicle):

    def info(self):
        print(self.name, self.max_speed, self.mileage)

Volvo = Bus("Volvo", 180, 12)

Volvo.info()
