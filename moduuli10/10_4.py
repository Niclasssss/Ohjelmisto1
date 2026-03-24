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

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def print_status(self):
        for car in self.cars:
            print(f"The {car.license_plate} is at {car.travelled_distance}.")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
            else:
                return False