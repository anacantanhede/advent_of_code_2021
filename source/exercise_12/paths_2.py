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

    all_paths = find_all_paths(graph, "start", "end", [])
    # print(all_paths)
    print(len(all_paths))


def no_other_double_small_caves(path, node):
    new_p = []
    for p in path:
        if p.lower() == p:
            if p != node and new_p.count(p) > 1:
                return False
            else:
                new_p.append(p)
    if sum([new_p.count(x) > 1 for x in new_p]) > 1:
        return False
    if node == "start" and node in path:
        return False
    if node == "end" and node in path:
        return False
    return True


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph.keys():
        return []
    paths = []
    for node in graph[start]:
        if (
            node not in path
            or node.upper() == node
            or (path.count(node) < 2 and no_other_double_small_caves(path, node))
        ):
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


if __name__ == "__main__":
    main()
