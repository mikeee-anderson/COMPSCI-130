def create_dictionary(usernames_list):
    dictionary = {}
    for username in usernames_list:
        if username[0] not in dictionary:
            dictionary[username[0]] = []
            dictionary[username[0]].append(username)
        else:
            dictionary[username[0]].append(username)
    return dictionary
data = create_dictionary(['mgra734', 'dng004', 'bcar035', 'myu134', 'dkim104'])
for key in sorted(data ):
    print(key, sorted(data[key]))