def main():
    with open("./input.txt", "r") as file:
        height = []
        for line in file:
            h = [int(x) for x in line.replace("\n", "")]
            height.append(h)

        basins = retrieve_basins(height)

        lenght_basins = []
        for b in basins:
            l = calculate_basin(height, {b})
            lenght_basins.append(len(l))
        top3 = []
        while len(top3) < 3:
            top3.append(max(lenght_basins))
            lenght_basins.remove(max(lenght_basins))
        result = 1
        for t in top3:
            result *= t
        print(result)


def calculate_basin(heights, basin):

    iterated = set()
    while (basin - iterated) != set():
        for b in list(basin - iterated):
            iterated.add(b)
            # print(f"iterating {b}, basin is {basin}, iterated {iterated}")
            init_y, init_x = b
            x = init_x
            y = init_y
            # traverse down
            while y < len(heights) - 1 and heights[y][init_x] < heights[y + 1][init_x]:
                basin.add((y, init_x))
                if heights[y + 1][init_x] != 9:
                    basin.add((y + 1, init_x))
                y += 1
            x = init_x
            y = init_y
            while y > 0 and heights[y][init_x] < heights[y - 1][init_x]:
                if heights[y - 1][init_x] != 9:
                    basin.add((y - 1, init_x))
                basin.add((y, init_x))
                y -= 1
            x = init_x
            y = init_y
            while (
                x < len(heights[0]) - 1 and heights[init_y][x] < heights[init_y][x + 1]
            ):
                basin.add((init_y, x))
                if heights[init_y][x + 1] != 9:
                    basin.add((init_y, x + 1))
                x += 1
            x = init_x
            y = init_y
            while x > 0 and heights[init_y][x] < heights[init_y][x - 1]:
                if heights[init_y][x - 1] != 9:
                    basin.add((init_y, x - 1))
                basin.add((init_y, x))
                x -= 1

    return basin


"""
    for b in basin:
        if b != current_coordinate:
            calculate_basin(heights, b, basin)
"""


def retrieve_basins(heights):
    # only retrieve the points which are lower than any of the adjacent points
    basins = []
    for y, line in enumerate(heights):
        for x, height in enumerate(line):
            if x == 0 and y == 0:
                if height < heights[y + 1][x] and height < heights[y][x + 1]:
                    basins.append((y, x))
            elif x == len(line) - 1 and y == len(heights) - 1:
                if height < heights[y - 1][x] and height < heights[y][x - 1]:
                    basins.append((y, x))
            elif x == len(line) - 1 and y == 0:
                if height < heights[y + 1][x] and height < heights[y][x - 1]:
                    basins.append((y, x))
            elif x == 0 and y == len(heights) - 1:
                if height < heights[y - 1][x] and height < heights[y][x + 1]:
                    basins.append((y, x))
            elif x == len(line) - 1:
                if (
                    height < heights[y - 1][x]
                    and height < heights[y + 1][x]
                    and height < heights[y][x - 1]
                ):
                    basins.append((y, x))
            elif x == 0:
                if (
                    height < heights[y - 1][x]
                    and height < heights[y + 1][x]
                    and height < heights[y][x + 1]
                ):
                    basins.append((y, x))
            elif y == 0:
                if (
                    height < heights[y + 1][x]
                    and height < heights[y][x - 1]
                    and height < heights[y][x + 1]
                ):
                    basins.append((y, x))
            elif y == len(heights) - 1:
                if (
                    height < heights[y - 1][x]
                    and height < heights[y][x - 1]
                    and height < heights[y][x + 1]
                ):
                    basins.append((y, x))
            elif (
                height < heights[y - 1][x]
                and height < heights[y + 1][x]
                and height < heights[y][x - 1]
                and height < heights[y][x + 1]
            ):
                basins.append((y, x))
    return basins


if __name__ == "__main__":
    main()
