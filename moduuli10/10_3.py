class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def go_to_floor(self, floor):
        self.current_floor = floor
        if self.current_floor > self.top_floor:
            self.current_floor = self.top_floor
        if self.current_floor < self.bottom_floor:
            self.current_floor = self.bottom_floor

    def floor_up(self):
        self.current_floor = self.current_floor + 1
        if self.current_floor > self.top_floor:
            self.current_floor = self.top_floor

    def floor_down(self):
        self.current_floor = self.current_floor - 1
        if self.current_floor < self.bottom_floor:
            self.current_floor = self.bottom_floor

class Building:
    def __init__(self, bottom_floor, top_floor, elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = []
        for _ in range(elevators):
            self.elevators.append(Elevator(bottom_floor, top_floor))

    def run_elevator(self, elevator_number, floor):
        self.elevators[elevator_number].go_to_floor(floor)

    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom_floor)