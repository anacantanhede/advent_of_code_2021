def main():
    diagram = [["."] * 10000 for x in range(10000)]

    with open("./input.txt", "r") as file:
        for line in file:
            try:
                x, y = [int(c) for c in line.replace("\n", "").split(",")]
                diagram[y][x] = "#"
            except Exception:
                if line.startswith("fold along y="):
                    fold_y = int((line.replace("\n", "").split("="))[1])
                    # print("fold y:", fold_y)
                    for index, _ in enumerate(diagram[fold_y]):
                        diagram[fold_y][index] = "-"

                    for horizontal in range(1, fold_y + 1):
                        for vertical, _ in enumerate(diagram[horizontal]):
                            if (
                                diagram[fold_y - horizontal][vertical] == "#"
                                or diagram[fold_y + horizontal][vertical] == "#"
                            ):
                                diagram[fold_y - horizontal][vertical] = "#"
                    for horizontal in range(len(diagram) - 1, fold_y - 1, -1):
                        diagram.pop(horizontal)
                    break
                elif line.startswith("fold along x="):
                    fold_x = int((line.replace("\n", "").split("="))[1])
                    # print("fold x:", fold_x)
                    for index_y, _ in enumerate(diagram):
                        diagram[index_y][fold_x] = "|"

                    for horizontal in range(len(diagram)):
                        for vertical in range(1, fold_x + 1):
                            if (
                                diagram[horizontal][fold_x - vertical] == "#"
                                or diagram[horizontal][fold_x + vertical] == "#"
                            ):
                                diagram[horizontal][fold_x - vertical] = "#"
                    for horizontal in range(len(diagram)):
                        for vertical in range(
                            len(diagram[horizontal]) - 1, fold_x - 1, -1
                        ):
                            diagram[horizontal].pop(vertical)
                    break
                else:
                    pass

        count_dots = 0
        for y in diagram:
            count_dots += y.count("#")
        print(count_dots)


if __name__ == "__main__":
    main()
