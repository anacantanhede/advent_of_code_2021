def main():
    with open("./input.txt", "r") as file:
        fish = [int(x) for x in file.readline().split(",")]
    # this is exponential... so it would take too much time
    # new approach...
    count_fishes = [0 * i for i in range(0, 9)]

    for f in fish:
        count_fishes[f] += 1

    for day in range(1, 257):
        # the 0 count move to position 8 and 6
        new_fishes = count_fishes[0]

        for i in range(1, 9):
            count_fishes[i - 1] = count_fishes[i]

        count_fishes[6] += new_fishes
        count_fishes[8] = new_fishes

    print(sum(count_fishes))


if __name__ == "__main__":
    main()
