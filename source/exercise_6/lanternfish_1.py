def main():
    with open("./input.txt", "r") as file:
        fish = [int(x) for x in file.readline().split(",")]

    for day in range(1, 81):
        new_fishes = []
        for index, f in enumerate(fish):
            if f > 0:
                fish[index] -= 1
            if f == 0:
                new_fishes.extend([8])
                fish[index] = 6
        fish.extend(new_fishes)
        # print(f"DAY {day}: {fish}")
    print(len(fish))


if __name__ == "__main__":
    main()
