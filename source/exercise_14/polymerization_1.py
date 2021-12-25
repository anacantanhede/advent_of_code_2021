def main():
    mapping = dict()
    initial = list()
    with open("./input.txt", "r") as file:
        for line in file:
            if line.count("->") == 0 and line.replace("\n", "").strip() != "":
                initial = line.replace("\n", "").strip()
            else:
                try:
                    i, out = line.replace("\n", "").split(" -> ")
                    mapping[i] = i[0] + out + i[1]
                except Exception:
                    pass

    print(initial)
    out = list()
    for step in range(1, 11):
        for i in range(0, len(initial) - 1):
            if i != len(initial) - 2:
                out.append(mapping[initial[i] + initial[i + 1]][0:2])
            else:
                out.append(mapping[initial[i] + initial[i + 1]])

        initial = "".join(out)
        out = list()
        # print(f"after step {step}: {initial}")
    count = {}
    for a in initial:
        count[a] = initial.count(a)

    print(max(count.values()) - min(count.values()))


if __name__ == "__main__":
    main()
