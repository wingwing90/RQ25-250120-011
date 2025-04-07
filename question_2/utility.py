# utility.py

# --- Field Class ---
class Field:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def in_bounds(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height


# --- Utils ---
direction_order = ['N', 'E', 'S', 'W']

def rotate_left(current):
    idx = direction_order.index(current)
    return direction_order[(idx - 1) % 4]

def rotate_right(current):
    idx = direction_order.index(current)
    return direction_order[(idx + 1) % 4]

def move_forward(x, y, direction):
    if direction == 'N':
        return x, y + 1
    elif direction == 'S':
        return x, y - 1
    elif direction == 'E':
        return x + 1, y
    elif direction == 'W':
        return x - 1, y
    return x, y


# --- Car Class ---
class Car:
    def __init__(self, name, x, y, direction, commands):
        self.name = name
        self.start_x = x
        self.start_y = y
        self.start_direction = direction

        self.x = x
        self.y = y
        self.direction = direction
        self.commands = commands

    def execute(self, command, field):
        if command == 'L':
            self.direction = rotate_left(self.direction)
        elif command == 'R':
            self.direction = rotate_right(self.direction)
        elif command == 'F':
            new_x, new_y = move_forward(self.x, self.y, self.direction)
            if field.in_bounds(new_x, new_y):
                self.x = new_x
                self.y = new_y