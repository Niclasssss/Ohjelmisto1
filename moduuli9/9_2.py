class Car:
    license_plate = 313
    maximum_speed = 142
    current_speed = 0
    travelled_distance = 0

    def __init__(self, Licenseplate, Maximumspeed):
        self.license_plate = Licenseplate
        self.maximum_speed = Maximumspeed

    def accelerate(self, määrä):
        self.current_speed += määrä
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0
