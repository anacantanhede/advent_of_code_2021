from sys import maxsize
from itertools import islice


def window(seq, n=2):
    "Returns a sliding window (of width n) over data from the iterable"
    "   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result


def strip_and_int(x):
    return int(x.strip())


with open("./1_input.txt") as file:
    line_list = file.readlines()

strip_line = list(map(strip_and_int, line_list))

previous_sum = maxsize
number_of_increases = 0
for slice in window(strip_line, 3):
    sum_slice = sum(slice)
    if sum_slice > previous_sum:
        number_of_increases += 1
    previous_sum = sum_slice

print(number_of_increases)
