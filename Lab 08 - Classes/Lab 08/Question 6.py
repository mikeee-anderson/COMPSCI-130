class LinearEquation:
    def __init__(self, coefficient_a = 1, coefficient_b = 1, coefficient_c = 1):
        self.coefficient_a = coefficient_a
        self.coefficient_b = coefficient_b
        self.coefficient_c = coefficient_c
    def __str__(self):
        a = self.coefficient_a
        b = self.coefficient_b
        c = self.coefficient_c
        return f"{a}x + {b}y = {c}"


equation1 = LinearEquation(1, 2, 1)
print(equation1.coefficient_a, equation1.coefficient_b, equation1.coefficient_c)
print(equation1)
equation2 = LinearEquation()
print(equation2.coefficient_a, equation2.coefficient_b, equation2.coefficient_c)
print(equation2)
