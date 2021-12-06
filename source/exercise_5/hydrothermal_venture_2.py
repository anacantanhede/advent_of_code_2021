def main():
    diagram = VectorDiagram()

    with open("./input.txt", "r") as file:
        for line in file:
            x1, y1, x2, y2 = line.replace(" -> ", ",").split(",")
            vector = Vector(Point(x1, y1), Point(x2, y2))
            # print(vector)
            diagram.add_vector(vector)
            # print(diagram)
        print(diagram.count_intersections())


class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __str__(self):
        return f"({self.x},{self.y})"

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_point(self):
        return self.x, self.y


class Vector:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def __str__(self):
        s = ""
        s += f"{self.point1} -> {self.point2}"
        return s

    def is_horizontal(self):
        if self.point1.get_y() == self.point2.get_y():
            return True
        return False

    def is_vertical(self):
        if self.point1.get_x() == self.point2.get_x():
            return True
        return False

    def smaller_x(self):
        if self.point1.get_x() > self.point2.get_x():
            return self.point2.get_x()
        return self.point1.get_x()

    def smaller_y(self):
        if self.point1.get_y() > self.point2.get_y():
            return self.point2.get_y()
        return self.point1.get_y()

    def bigger_x(self):
        if self.point1.get_x() > self.point2.get_x():
            return self.point1.get_x()
        return self.point2.get_x()

    def bigger_y(self):
        if self.point1.get_y() > self.point2.get_y():
            return self.point1.get_y()
        return self.point2.get_y()

    def get_point1(self):
        return self.point1.get_point()

    def get_point2(self):
        return self.point2.get_point()


class VectorDiagram:
    def __init__(self):
        self.diagram = [[0] * 1000 for _ in range(1000)]

    def __str__(self):
        s = ""
        for l in self.diagram:
            s += f"{str(l)}\n"
        return s

    def add_vector(self, vector):
        if vector.is_horizontal():
            start = int(vector.smaller_x())
            end = int(vector.bigger_x())
            for i in range(start, end + 1, 1):
                self.diagram[vector.point1.get_y()][i] += 1
        elif vector.is_vertical():
            start = int(vector.smaller_y())
            end = int(vector.bigger_y())
            for i in range(start, end + 1, 1):
                self.diagram[i][vector.point1.get_x()] += 1
        # there are only horizontal, vertical or diagonal lines
        else:
            x1, y1 = vector.get_point1()
            x2, y2 = vector.get_point2()
            if x1 <= x2:
                range_x = range(x1, x2 + 1, 1)
            else:
                range_x = range(x1, x2 - 1, -1)

            if y1 <= y2:
                range_y = range(y1, y2 + 1, 1)
            else:
                range_y = range(y1, y2 - 1, -1)

            for y, x in zip(range_y, range_x):
                self.diagram[y][x] += 1

    def count_intersections(self):
        count = 0
        for line in self.diagram:
            count += len([x for x in line if x >= 2])
        return count


if __name__ == "__main__":
    main()
