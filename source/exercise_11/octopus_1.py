from collections import deque


def main():
    with open("./input.txt", "r") as file:
        octo = []
        for line in file:
            h = [int(x) for x in line.replace("\n", "")]
            octo.append(h)
    count = 0
    for i in range(0, 100):
        # print(f"After round {i+1}")
        count += one_round(octo)
        # print(count)
    print(count)


def exists_adjacent(lst, line_index, column_index):
    if line_index == -1 or column_index == -1:
        return False
    try:
        lst[line_index][column_index]
    except Exception as e:
        return False
    return True


def one_round(map):
    for line_index, line in enumerate(map):
        for column_index, o in enumerate(line):
            map[line_index][column_index] += 1

    flashed = set()
    new_found = True
    while new_found:
        new_found = False
        for line_index, line in enumerate(map):
            for column_index, o in enumerate(line):
                if o >= 10 and ((line_index, column_index) not in flashed):
                    flashed.add((line_index, column_index))
                    new_found = True
                    for adjacent_line in range(line_index - 1, line_index + 2, 1):
                        for adjacent_column in range(
                            column_index - 1, column_index + 2, 1
                        ):
                            if exists_adjacent(map, adjacent_line, adjacent_column):
                                map[adjacent_line][adjacent_column] += 1
                    map[line_index][column_index] -= 1
    c = 0
    for line_index, line in enumerate(map):
        for column_index, o in enumerate(line):
            if o > 9:
                map[line_index][column_index] = 0
                c += 1
    return c


if __name__ == "__main__":
    main()
