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

class ElectricCar(Car):
    def __init__(self, license_plate, maximum_speed, battery_capacity):
        super().__init__(license_plate, maximum_speed)
        self.battery_capacity = battery_capacity


class GasolineCar(Car):
    def __init__(self, license_plate, maximum_speed, tank_volume):
        super().__init__(license_plate, maximum_speed)
        self.tank_volume = tank_volume