class SubmarineCondition:
    def __init__(self):
        self.power_consumption = None
        self.gamma_rate = None
        self.epsilon_rate = None

    def _binary_list_to_decimal(self, binary_list):
        decimal = 0
        lenght_list = len(binary_list)
        for i in range(lenght_list)[::-1]:
            decimal += binary_list[i] * (2 ** (lenght_list - 1 - i))
        return decimal

    def determine_gamma_rate(self, input):
        # most common bit of each position from all numbers
        temp_gamma_rate = [0] * len(input[0])
        for i in range(len(input[0])):
            count_0 = [column[i] for column in input].count("0")
            count_1 = [column[i] for column in input].count("1")
            if count_1 > count_0:
                temp_gamma_rate[i] = 1
        self.gamma_rate = self._binary_list_to_decimal(temp_gamma_rate)
        return self.gamma_rate

    def determine_epsilon_rate(self, input):
        # least common bit of each position from all numbers
        temp_epsilon_rate = [0] * len(input[0])
        for i in range(len(input[0])):
            count_0 = [column[i] for column in input].count("0")
            count_1 = [column[i] for column in input].count("1")
            if count_1 < count_0:
                temp_epsilon_rate[i] = 1
        self.epsilon_rate = self._binary_list_to_decimal(temp_epsilon_rate)
        return self.epsilon_rate

    def determine_power_consumption(self):
        self.power_consumption = self.gamma_rate * self.epsilon_rate
        return self.power_consumption


condition = SubmarineCondition()
input = []
with open("./input.txt", "r") as file:
    for line in file:
        input.append(list(line.replace("\n", "")))

print(condition.determine_gamma_rate(input))
print(condition.determine_epsilon_rate(input))
print(condition.determine_power_consumption())
