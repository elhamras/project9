class Car:
    def __init__(self, register_number, Max_speed, travel_distance, current_speed):
        self.register_number = register_number
        self.Max_speed = Max_speed
        self.travel_distance = travel_distance
        self.current_speed = current_speed


    def acpect(self):
        return (f"register number: {self.register_number} , max speed: {self.Max_speed}")


    def accerelate(self,change_speed):
        self.change_speed = change_speed
        while self.current_speed >= 0 and self.current_speed <= self.Max_speed:
            change_speed = int(input("Enter new speed : "))
            if change_speed == -200:
                print(f"final speed : {self.current_speed}")
                break
            elif change_speed > self.Max_speed:
                print("The speed over the max speed")
            else:
                self.current_speed = self.current_speed + change_speed
            if self.current_speed < self.Max_speed:
                print(f"current speed is : {self.current_speed}")
            elif self.current_speed > self.Max_speed:
                print("The speed over the max speed")

    def drive(self, hour):
        self.travel_distance = self.travel_distance + 60 * hour
        return self.travel_distance





TOYOTA = Car("ABC-123",142,0,0)
TOYOTA.travel_distance = 2000
print(TOYOTA.acpect())
TOYOTA.drive(1.5)
print(f"new distance is : {TOYOTA.travel_distance}")
