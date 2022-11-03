import random


def count_rolls_until_6():
    res = random.choice([1, 2, 3, 4, 5, 6])
    # print(res)
    count_rolls = 1
    while res != 6:
        res = random.choice([1, 2, 3, 4, 5, 6])
        # print(res)
        count_rolls = count_rolls + 1

    return count_rolls


days = [i for i in range(1, 32)]
months = [i for i in range(1, 13)]


def birthday(day, month):
    i = random.choice(months)
    j = random.choice(days)
    counter = 1
    while i != month and j != day:
        i = random.choice(months)
        j = random.choice(days)
        counter = counter + 1
    return counter


day = 19
month = 5
print("It took", birthday(day, month), "trials to draw this birthday:", day, ".", month)