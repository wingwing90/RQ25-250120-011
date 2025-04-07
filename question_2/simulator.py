# simulator.py
from utility import Car, Field

class Simulator:
    def __init__(self):
        self.cars = []
        self.field = None

    def create_field(self, width, height):
        self.field = Field(width, height)

    def add_car(self, name, x, y, direction, commands):
        car = Car(name, x, y, direction, commands)
        self.cars.append(car)

    def reset(self):
        self.cars = []
        self.field = None

    def list_cars(self):
        return [str(car) for car in self.cars]

    def run(self):
        positions = {car.name: car.position() for car in self.cars}
        car_status = {car.name: car for car in self.cars}
        max_steps = max(len(car.commands) for car in self.cars)

        for step in range(max_steps):
            moved_positions = {}
            for car in self.cars:
                if not car.active:
                    continue
                prev_pos = car.position()
                car.step(self.field)
                new_pos = car.position()

                if new_pos in moved_positions.values():
                    # Collision detected
                    for other_name, other_pos in moved_positions.items():
                        if other_pos == new_pos:
                            car.collided = True
                            car.active = False
                            car_status[other_name].collided = True
                            car_status[other_name].active = False
                            print(f"- {car.name}, collides with {other_name} at {new_pos} at step {step + 1}")
                            print(f"- {other_name}, collides with {car.name} at {new_pos} at step {step + 1}")
                else:
                    moved_positions[car.name] = new_pos

        # Output final state
        for car in self.cars:
            if not car.collided:
                print(f"- {car.name}, ({car.x},{car.y}) {car.direction}")
