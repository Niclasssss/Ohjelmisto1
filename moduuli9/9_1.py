class Car:
    license_plate = 313
    maximum_speed = 142
    current_speed = 0
    travelled_distance = 0

    def __init__(self, Licenseplate, Maximumspeed):
        self.license_plate = Licenseplate
        self.maximum_speed = Maximumspeed

car = Car("ABC-123", 142)
print(f"License plate: {car.license_plate}")
print(f"Maximum speed: {car.maximum_speed} km/h")
print(f"Current speed: {car.current_speed} km/h")
print(f"Travelled distance: {car.travelled_distance} km")