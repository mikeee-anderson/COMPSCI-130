def create_triangles_list(numbers_list):
    triangles = []
    for numbers in numbers_list:
        side_a, side_b, side_c = numbers

    if is_triangle(side_a, side_b, side_c):
        triangle = Triangle(side_a, side_b, side_c)
        triangles.append(triangle)
    return triangles



