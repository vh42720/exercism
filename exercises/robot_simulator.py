# Globals for the directions
# Change the values as you see fit
EAST = [1, 0]
NORTH = [0, 1]
WEST = [-1, 0]
SOUTH = [0, -1]


class Robot:
    def __init__(self, direction=None, x=0, y=0):
        if direction is None:
            direction = NORTH
        self.direction, self.x, self.y = direction, x, y
        self.coordinates = (self.x, self.y)

    def move(self, steps):
        for step in steps:
            # turning right is rotating the vector clockwise
            if step == 'R':
                self.direction = [self.direction[1], -self.direction[0]]
            elif step == 'L':
                self.direction = [-self.direction[1], self.direction[0]]
            elif step == 'A':
                self.coordinates = (self.coordinates[0] + self.direction[0],
                                    self.coordinates[1] + self.direction[1])
