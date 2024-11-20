
def bubble_sort(data):
    for pass_num in range(len(data) - 1, 0, -1):
        for i in range(0, pass_num):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]

def bubble_sort_fast(lst):
    n = len(lst)
    comparisons = 0
    swaps = 0

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparisons += 1
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swaps += 1
                swapped = True
        if not swapped:
            break

    return n, comparisons, swaps



d1 = [12, 15, 19, 37, 39]
result1 = bubble_sort(d1)
print('Normal Bubble Sort: Length: {} Comparisons: {} Swaps: {}'.format(result1[0], result1[1], result1[2]))
d2 = [12, 15, 19, 37, 39]
result2 = bubble_sort_fast(d2)
print('Fast Bubble Sort: Length: {} Comparisons: {} Swaps: {}'.format(result2[0], result2[1], result2[2]))
