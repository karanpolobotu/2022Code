# create a vehicle class w/ attriutes max_speed and mileage instance attributes

class Vehicle:
# created class!

    def __init__(self, max_speed, mileage):
    #created constructor
        self.max_speed = max_speed
        self.mileage = mileage

#creating object

modelX = Vehicle(10, 10)

print("instance var 1: ", modelX.max_speed)

print("instance var 2: ", modelX.mileage)
