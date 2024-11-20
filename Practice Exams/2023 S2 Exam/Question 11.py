class Roman:
    roman_dict = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100}

    def __init__(self, codes_list):
        self.codes_list = codes_list
        self.values = self.caclculate_values(codes_list)

    def caclculate_values(self, codes_list):
        total = 0
        for code in self.codes_list:
            value = self.roman_dict[code]
            total += value
        return total

    def __str__(self):
        return f"{''.join(self.codes_list)}({self.values})"

    def __lt__(self, other):
        return self.values < other.values


roman1 = Roman(['X', 'X', 'I'])
roman2 = Roman(['C', 'I'])
print(roman1, roman2)
print(type(roman1))
print(roman1 < roman2)
print(roman2 < roman1)

        

