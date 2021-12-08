def main():
    seg = []
    count = 0
    with open("./input.txt", "r") as file:
        for line in file:
            seg = list([x for x in line.replace("\n", "").split(" | ")][1].split())
            for s in seg:
                if len(s) in (2, 3, 4, 7):
                    count += 1
        print(count)


if __name__ == "__main__":
    main()
