def main():
    open_list = ("[", "(", "{", "<")
    close_list = ("]", ")", "}", ">")
    scores = list()
    with open("./input.txt", "r") as file:
        for line in file:
            symbols = list(line.replace("\n", ""))
            # print(symbols)
            list_of_opened = list()
            corrupted = False
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
                        # corrupted_characters.append(s)
                        corrupted = True
                        break

            if len(list_of_opened) > 0 and not corrupted:
                # print(f"Incomplete Line: {list_of_opened}")
                calculate_closure = list()
                for s in list_of_opened[::-1]:
                    calculate_closure.append(close_list[open_list.index(s)])
                # print(f"Characters Needed to Close Line: {calculate_closure}")

                count = 0
                for c in calculate_closure:
                    count *= 5
                    if c == ")":
                        count += 1
                    elif c == "]":
                        count += 2
                    elif c == "}":
                        count += 3
                    elif c == ">":
                        count += 4
                    else:
                        print("WRONG CORRUPTED CHARACTER")
                # print(count)
                scores.append(count)
    sorted_scores = sorted(scores)

    print(sorted_scores[int((len(scores) - 1) / 2)])


if __name__ == "__main__":
    main()
