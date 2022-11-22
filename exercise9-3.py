class Car:

    def __init__(self, registration_number, maximum_speed, current_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
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

    def drive(self, hour):
        self.travelled_distance += self.current_speed * hour


car = Car("ABC-123", 142, 60)
car.drive(1.5)
print(f"the new distance is: {car.travelled_distance} km.")