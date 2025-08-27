import random
rand_list = []

for i in range(10):
    rand_list.append(random.randint(1, 20))

list_comprehension_below_10 = [n for n in rand_list if n < 10]

def filter_number(number):
    if number < 10:
        return True
    return False

list_comprehension_below_10 = list(filter(filter_number, rand_list))

