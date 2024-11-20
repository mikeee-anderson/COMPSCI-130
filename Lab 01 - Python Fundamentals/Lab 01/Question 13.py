names = ['abal412', 'oabc399', 'oyi001']
def get_sum_last_digits(usernames):
    return sum(int(username[-1]) for username in usernames)


print(get_sum_last_digits(names))