def get_row_sums(matrix) :
    return [sum(x) for x in matrix]

data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(get_row_sums(data))
print(get_row_sums([[1, 2],[7, 6]]))
print(get_row_sums([[3, 5],[2, 6]]))