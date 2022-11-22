import random
from random import random

class car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

car = car("ABC-123", 142)
print(f"The car's registration number is: {car.registration_number}, the maximum speed is: {car.maximum_speed}")
print(f"The current speed is: {car.current_speed} and the travelled distance is: {car.travelled_distance}")