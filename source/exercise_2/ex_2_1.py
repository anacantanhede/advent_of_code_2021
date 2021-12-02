class SubmarinePosition:
    def __init__(self):
        self.horizontal_position = 0
        self.depth = 0

    def move(self, direction, value):
        if direction == "forward":
            self.horizontal_position += int(value)
        elif direction == "down":
            self.depth += int(value)
        elif direction == "up":
            self.depth -= int(value)
        else:
            print("INVALID DIRECTION: ", direction)
        return self

    def end_position(self):
        return self.horizontal_position * self.depth


position = SubmarinePosition()
with open("./input.txt") as file:
    for line in file:
        direction, value = line.split()
        position.move(direction, int(value))
    print(position.end_position())
