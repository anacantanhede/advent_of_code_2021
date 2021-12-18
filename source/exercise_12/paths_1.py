def main():
    graph = dict()
    with open("./input.txt", "r") as file:
        for line in file:
            a, b = line.replace("\n", "").split("-")
            # print(f"{a} --> {b}")
            try:
                graph[a].add(b)
            except KeyError:
                graph[a] = {b}

            try:
                graph[b].add(a)
            except KeyError:
                graph[b] = {a}

    # print(graph)
    all_paths = find_all_paths(graph, "start", "end", [])
    print(len(all_paths))


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph.keys():
        return []
    paths = []
    for node in graph[start]:
        if node not in path or node.upper() == node:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


if __name__ == "__main__":
    main()
