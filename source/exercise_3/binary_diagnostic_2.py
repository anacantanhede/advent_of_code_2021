class SubmarineCondition:
    def __init__(self):
        self.power_consumption = None
        self.gamma_rate = None
        self.gamma_rate_binary = None
        self.epsilon_rate = None
        self.life_support_rating = None
        self.oxygen_generator_rating = None
        self.co2_scrubber_rating = None

    def _binary_list_to_decimal(self, binary_list):
        decimal = 0
        lenght_list = len(binary_list)
        for i in range(lenght_list)[::-1]:
            decimal += binary_list[i] * (2 ** (lenght_list - 1 - i))
        return decimal

    def determine_gamma_rate(self, input):
        # most common bit of each position from all numbers
        temp_gamma_rate = 0
        for i in range(len(input[0])):
            count_1 = [column[i] for column in input].count("1")
            if count_1 * 2 > len(input):
                temp_gamma_rate += 1 * (2 ** (len(input[0]) - 1 - i))
        self.gamma_rate = temp_gamma_rate
        return self.gamma_rate

    def determine_epsilon_rate(self, input):
        # least common bit of each position from all numbers
        temp_epsilon_rate = 0
        for i in range(len(input[0])):
            count_1 = [column[i] for column in input].count("1")
            if count_1 * 2 < len(input):
                temp_epsilon_rate += 1 * (2 ** (len(input[0]) - 1 - i))
        self.epsilon_rate = temp_epsilon_rate
        return self.epsilon_rate

    def determine_power_consumption(self):
        self.power_consumption = self.gamma_rate * self.epsilon_rate
        return self.power_consumption

    def _determine_most_common_bit(self, input, position):
        length = len(input)
        count_0 = [column[position] for column in input].count("0")
        # If 0 and 1 are equally common, keep values with a 1
        if count_0 * 2 > len(input):
            return 0
        else:
            return 1

    def _determine_least_common_bit(self, input, position):
        length = len(input)
        count_0 = [column[position] for column in input].count("0")
        # If 0 and 1 are equally common, keep values with a 0
        if count_0 * 2 <= len(input):
            return 0
        else:
            return 1

    def determine_oxygen_generator_rating(self, input):
        filtered_input = input.copy()
        for i in range(len(input[0])):
            most_common = self._determine_most_common_bit(filtered_input, i)
            filtered_input[:] = [x for x in filtered_input if x[i] == str(most_common)]
            if (len(filtered_input)) <= 1:
                break
        self.oxygen_generator_rating = self._binary_list_to_decimal(
            [int(x) for x in filtered_input[0]]
        )
        return self.oxygen_generator_rating

    def determine_co2_scrubber_rating(self, input):
        filtered_input = input.copy()
        for i in range(len(input[0])):
            least_common = self._determine_least_common_bit(filtered_input, i)
            filtered_input[:] = [x for x in filtered_input if x[i] == str(least_common)]
            if (len(filtered_input)) <= 1:
                break
        self.co2_scrubber_rating = self._binary_list_to_decimal(
            [int(x) for x in filtered_input[0]]
        )
        return self.co2_scrubber_rating

    def determine_life_support_rating(self):
        self.life_support_rating = (
            self.oxygen_generator_rating * self.co2_scrubber_rating
        )
        return self.life_support_rating


condition = SubmarineCondition()
input = []
with open("./input.txt", "r") as file:
    for line in file:
        input.append(list(line.replace("\n", "")))

print(condition.determine_gamma_rate(input))
print(condition.determine_epsilon_rate(input))
print(condition.determine_power_consumption())
print(condition.determine_oxygen_generator_rating(input))
print(condition.determine_co2_scrubber_rating(input))
print(condition.determine_life_support_rating())
