class Car:
    def __init__(self, Licenseplate, Maximumspeed):
        self.license_plate = Licenseplate
        self.maximum_speed = Maximumspeed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, määrä):
        self.current_speed += määrä
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, tuntimäärä):
        self.travelled_distance =+ tuntimäärä * self.current_speed

car = Car("ABC-123", 142)
print(f"Initial distance: {car.travelled_distance} km")
car.current_speed = 60
car.drive(1.5)
print(f"Distance after driving 1.5 hours at 60 km/h: {car.travelled_distance} km")