my_list = [0, 5, -5, 15, 50, 10, 2]
def sum_of_scores(scores):
    try:
        total = 0
        for score in scores:
            if score > 0 and score < 10:
                total += score
        return total
    except TypeError:
        return total
    except ValueError:
        return total


print(sum_of_scores(my_list))
my_list = [1, 2, 13, 4, "two", 2, 9]
print(sum_of_scores(my_list))
print(sum_of_scores([]))
print(sum_of_scores(['NA']))