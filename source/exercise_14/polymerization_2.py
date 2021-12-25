def main():
    mapping = dict()
    initial = dict()
    with open("./input.txt", "r") as file:
        for line in file:
            if line.count("->") == 0 and line.replace("\n", "").strip() != "":
                template = line.replace("\n", "").strip()
                for i in range(0, len(template) - 1):
                    if template[i] + template[i + 1] not in initial.keys():
                        initial[template[i] + template[i + 1]] = 1
                    else:
                        initial[template[i] + template[i + 1]] += 1
                # initial[template[-1]] = 1
            else:
                try:
                    i, out = line.replace("\n", "").split(" -> ")
                    mapping[i] = i[0] + out + i[1]
                    if i not in initial.keys():
                        initial[i] = 0
                except Exception:
                    pass

    print(initial)
    out = dict()
    for k in initial.keys():
        out[k] = 0
    for step in range(1, 41):
        for k, v in initial.items():
            if v > 0:
                out[mapping[k][0:2]] += v
                out[mapping[k][1:3]] += v
        initial = out.copy()
        for k in initial.keys():
            out[k] = 0
        print(f"after step {step}: {initial}")
    count = {}
    for a in initial:
        try:
            count[a[0]] += initial[a]
        except:
            count[a[0]] = initial[a]
        try:
            count[a[1]] += initial[a]
        except:
            count[a[1]] = initial[a]
    for c in count.keys():
        if c == template[0] or c == template[-1]:
            count[c] = int((count[c] + 1) / 2)
        else:
            count[c] = int((count[c]) / 2)
    print(count)
    print(max(count.values()) - min(count.values()))


if __name__ == "__main__":
    main()
