previous_line = 9999999
number_of_increases = 0

with open("./1_input.txt") as file:
    for line in file:
        if int(line) - previous_line > 0:
            number_of_increases += 1
        previous_line = int(line)

print(number_of_increases)
