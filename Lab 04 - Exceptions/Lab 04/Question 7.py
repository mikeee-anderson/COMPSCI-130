my_list = [-1, 0, 5, 2, 'ten', 35, 45, 9, 20]
def sum_of_scores_continue(scores):
    total = 0
    for score in scores:
        try:
            if score > 0 and score < 10:
                total += score
        except TypeError:
            pass
        except ValueError:
            pass
    return total

print(sum_of_scores_continue(my_list))
print(sum_of_scores_continue([-1, 0, 10, 20, 'ten', 35, 45, 105, 20]))
my_list = [1, 2, 3, 4, "two", 2]
print(sum_of_scores_continue(my_list))