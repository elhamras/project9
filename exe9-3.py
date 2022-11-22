class Car:
    def __init__(self, register_number, Max_speed, travel_distance, current_speed):
        self.register_number = register_number
        self.Max_speed = Max_speed
        self.travel_distance = travel_distance
        self.current_speed = current_speed


    def acpect(self):
        return (f"register number: {self.register_number} , max speed: {self.Max_speed}")

    def drive(self, hour):
        self.travel_distance = self.travel_distance + 60 * hour
        return self.travel_distance

TOYOTA = Car("ABC-123",142,0,0)
TOYOTA.travel_distance = 2000
print(TOYOTA.acpect())
TOYOTA.drive(1.5)
print(f"new distance is : {TOYOTA.travel_distance}")