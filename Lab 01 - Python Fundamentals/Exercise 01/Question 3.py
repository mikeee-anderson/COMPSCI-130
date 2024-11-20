a_list = ['coderunner', 'auckland', 'ac', 'nz']
def get_string(words):
    seperator = "."
    website = seperator.join(words)
    return website


print(get_string(a_list))