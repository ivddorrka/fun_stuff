import random

def read_file(file):
    file_open = open(file, "r")
    file_lst = file_open.readlines()
    file_list = ''.join(map(str, file_lst)).split('\n')
    file_open.close()
    return file_list
# print(read_file('monday'))

def random_quote(file):
    list_quotes = read_file(file)
    return random.choice(list_quotes)
print(random_quote('monday'))
