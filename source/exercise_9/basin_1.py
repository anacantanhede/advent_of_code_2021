def main():
    with open("./input.txt", "r") as file:
        height = []
        for line in file:
            h = [int(x) for x in line.replace("\n", "")]
            height.append(h)

        print(retrieve_lower(height))


def retrieve_lower(heights):
    # only retrieve the points which are lower than any of the adjacent points
    lower = 0
    for y, line in enumerate(heights):
        for x, height in enumerate(line):
            if x == 0 and y == 0:
                if height < heights[y + 1][x] and height < heights[y][x + 1]:
                    lower += height + 1
            elif x == len(line) - 1 and y == len(heights) - 1:
                if height < heights[y - 1][x] and height < heights[y][x - 1]:
                    lower += height + 1
            elif x == len(line) - 1 and y == 0:
                if height < heights[y + 1][x] and height < heights[y][x - 1]:
                    lower += height + 1
            elif x == 0 and y == len(heights) - 1:
                if height < heights[y - 1][x] and height < heights[y][x + 1]:
                    lower += height + 1
            elif x == len(line) - 1:
                if (
                    height < heights[y - 1][x]
                    and height < heights[y + 1][x]
                    and height < heights[y][x - 1]
                ):
                    lower += height + 1
            elif x == 0:
                if (
                    height < heights[y - 1][x]
                    and height < heights[y + 1][x]
                    and height < heights[y][x + 1]
                ):
                    lower += height + 1
            elif y == 0:
                if (
                    height < heights[y + 1][x]
                    and height < heights[y][x - 1]
                    and height < heights[y][x + 1]
                ):
                    lower += height + 1
            elif y == len(heights) - 1:
                if (
                    height < heights[y - 1][x]
                    and height < heights[y][x - 1]
                    and height < heights[y][x + 1]
                ):
                    lower += height + 1
            elif (
                height < heights[y - 1][x]
                and height < heights[y + 1][x]
                and height < heights[y][x - 1]
                and height < heights[y][x + 1]
            ):
                lower += height + 1
    return lower


if __name__ == "__main__":
    main()
