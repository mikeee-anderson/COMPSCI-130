def is_triangle(side_length_a, side_length_b, side_length_c):
    return (side_length_a + side_length_b) > side_length_c and (side_length_a + side_length_c) > side_length_b and (side_length_b + side_length_c) > side_length_a



print(is_triangle(4, 8, 17))
print(is_triangle(14, 8, 5))
print(is_triangle(14, 8, 25))