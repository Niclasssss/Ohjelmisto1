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