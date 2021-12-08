from itertools import permutations


def main():
    with open("./input.txt", "r") as file:
        total = 0
        for line in file:
            # print(line)

            seg_input = [x for x in line.replace("\n", "").split(" | ")][0].split()

            # we know that certain translation key will lead to an understandable output
            translation = {}
            keys = ["a", "b", "c", "d", "e", "f", "g"]
            values = ["a", "b", "c", "d", "e", "f", "g"]
            perm_values = permutations(values)

            max_matches = 0
            translation_max_matches = {}
            copy_input = seg_input.copy()
            for p in list(perm_values):
                translation = {k: v for k, v in zip(list(keys), list(p))}
                m = number_of_matches(copy_input, translation)
                if m > max_matches:
                    translation_max_matches = translation
                    max_matches = m
                    if m == 10:
                        break
            # print("MATCHES: ", max_matches)
            # print("TRANSLATION:", translation_max_matches)

            seg_output = [x for x in line.replace("\n", "").split(" | ")][1].split()
            total += calculate_output(seg_output, translation_max_matches)
    print(total)


def number_of_matches(sequence, translation):
    count_matches = 0
    for s in sequence:
        copy_s = "".join(sorted("".join(s.translate(s.maketrans(translation)))))
        n = number_based_on_sequence(copy_s)
        if n is not None:
            count_matches += 1
    return count_matches


def match_found(sequence, translation):
    # print(sequence)
    # print(translation)
    for s in sequence:
        copy_s = "".join(sorted("".join(s.translate(s.maketrans(translation)))))
        n = number_based_on_sequence(copy_s)
        print(copy_s, "MATCHED TO ", n)
        if n is None:
            # print("could not find match from: ", sequence, " to ", copy_s)
            return False
    return True


def calculate_output(sequence, translation):
    hidden_number = 0
    for s in sequence:
        copy_s = "".join(sorted("".join(s.translate(s.maketrans(translation)))))
        # print("TRANSLATED OUTPUT: ", (copy_s))
        hidden_number *= 10
        n = number_based_on_sequence(copy_s)
        if n is None:
            print("COULD NOT FIND MATCH FOR", copy_s)
        else:
            hidden_number += n
    return hidden_number


def is_match(sequence):
    if number_based_on_sequence(sequence) is not None:
        return True
    else:
        return False


def number_based_on_sequence(sequence):
    if sequence == "abcefg":
        return 0
    elif sequence == "cf" or len(sequence) == 2:
        return 1
    elif sequence == "acdeg":
        return 2
    elif sequence == "acdfg":
        return 3
    elif sequence == "bcdf" or len(sequence) == 4:
        return 4
    elif sequence == "abdfg":
        return 5
    elif sequence == "abdefg":
        return 6
    elif sequence == "acf" or len(sequence) == 3:
        return 7
    elif sequence == "abcdefg" or len(sequence) == 7:
        return 8
    elif sequence == "abcdfg":
        return 9
    else:
        return None


def check_match_by_len(input):
    if len(input) == 2:
        return 1
    elif len(input) == 3:
        return 7
    elif len(input) == 4:
        return 4
    elif len(input) == 7:
        return 8
    return None


if __name__ == "__main__":
    main()
