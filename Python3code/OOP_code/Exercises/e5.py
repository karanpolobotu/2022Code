# define a class attribute "color" with a default value white

class Vehicle:
    
    color = "White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def show(self):

        #call class variable
        print(Vehicle.color, self.name, self.max_speed, self.mileage)

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

# modify class variable when creating object

Volvo = Car("Volvo", 10, 1)
Volvo.show()

Audi = Car("Audi Q5", 10, 5)
Vehicle.color = "Blue"
Audi.show()
