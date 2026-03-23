import random

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
        self.travelled_distance += tuntimäärä * self.current_speed

cars = []
def race(cars):
    while True:
        for car in cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)
        if car.travelled_distance >= 10000:
            return cars