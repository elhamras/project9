import random
from random import random

class car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accerelate(self, speed_change):
        new_speed = car.current_speed + speed_change
        if new_speed < 0:
            self.current_speed = 0
        elif self.maximum_speed > new_speed and new_speed > 0:
            self.current_speed += speed_change

    def brake(self):
        if self.current_speed > 200:
            self.current_speed -= 200
        print("Emergency Brake!")


car = car("ABC-123", 142)
car.accerelate(+30)
print(f"The current speed is: {car.current_speed} km/h")
car.accerelate(+70)
print(f"The current speed is: {car.current_speed} km/h")
car.accerelate(+50)
print(f"The current speed is: {car.current_speed} km/h")
car.accerelate(200)
print(f"The current speed is: {car.current_speed} km/h")