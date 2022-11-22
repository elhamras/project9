class Car:
    def __init__(self, registration_number, maximum_speed, current_speed, travelled_distance):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def asspect(self):
        print(f" registration_number :{self.registration_number}, maximum_speed :{self.maximum_speed} ")

new = Car(ABC-123 ,142, 0, 0)