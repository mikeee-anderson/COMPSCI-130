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
    def is_parallel(self, other):
        return self.coefficient_a / self.coefficient_b == other.coefficient_a / other.coefficient_b
    def solve_for_y(self, x):
        return (self.coefficient_c - self.coefficient_a * x) / self.coefficient_b
    def solve_for_x(self, y):
        return (self.coefficient_c - self.coefficient_b * y) / self.coefficient_a

equation1 = LinearEquation(1, 2, 1)
print(equation1.coefficient_a, equation1.coefficient_b, equation1.coefficient_c)
print(equation1)
equation2 = LinearEquation()
print(equation2.coefficient_a, equation2.coefficient_b, equation2.coefficient_c)
print(equation2)
print(equation1.solve_for_y(2))
print(equation1.solve_for_x(1))
equation2 = LinearEquation(2, 3, 5)
equation1 = LinearEquation(4, 6, 10)
equation3 = LinearEquation(3, 2, 5)
print(equation1.is_parallel(equation2))
print(equation1.is_parallel(equation3))
print(equation2.is_parallel(equation1))
print(equation1.solve_for_y(4))
print(equation1.solve_for_x(2))

