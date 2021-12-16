def main():
    open_list = ("[", "(", "{", "<")
    close_list = ("]", ")", "}", ">")
    corrupted_characters = list()
    with open("./input.txt", "r") as file:
        for line in file:
            symbols = list(line.replace("\n", ""))
            # print(symbols)
            list_of_opened = list()
            for s in symbols:
                if s in open_list:
                    list_of_opened.extend(s)
                    # print(f"list of opened: {list_of_opened}")
                elif s in close_list:
                    if open_list[close_list.index(s)] == list_of_opened[-1]:
                        list_of_opened.pop()
                        # print(f"list of opened: {list_of_opened}")
                    else:
                        # print(f"CORRUPTED: {symbols}")
                        corrupted_characters.append(s)
                        break
    print(corrupted_characters)
    count = 0
    for c in corrupted_characters:
        if c == ")":
            count += 3
        elif c == "]":
            count += 57
        elif c == "}":
            count += 1197
        elif c == ">":
            count += 25137
        else:
            print("WRONG CORRUPTED CHARACTER")
    print(count)


if __name__ == "__main__":
    main()
