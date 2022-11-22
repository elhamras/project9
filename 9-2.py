class car:
    def __init__(self, registration_number, maximum_speed, current_speed, travelled_distance):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def acpect(self):
        return (f"registration number is: {self.registration_number} , maximum speed is: {self.maximum_speed}")

    def accerelate(self, change_speed):
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

TOYOTA = car("ABC-123",142,0,0)
print(TOYOTA.acpect())
TOYOTA.accerelate()

