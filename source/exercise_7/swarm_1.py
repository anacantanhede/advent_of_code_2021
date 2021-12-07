def main():
    with open("./test_input.txt", "r") as file:
        crabs = [int(x) for x in file.readline().split(",")]

    least_fuel = None
    for position in range(0, max(crabs) + 1):
        current_fuel = 0
        for i in crabs:
            current_fuel += abs(i - position)
        if least_fuel == None or current_fuel < least_fuel:
            least_fuel = current_fuel
    print(least_fuel)


if __name__ == "__main__":
    main()
