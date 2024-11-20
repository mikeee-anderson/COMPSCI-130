def get_words(usernames_list):
    return [username[:4] if len(username) == 7 else username[:3] for username in usernames_list]


print(get_words(['mgra734', 'dng004', 'bcar035']))
print(get_words(['myu134', 'dkim104']))