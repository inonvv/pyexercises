import random

def count_rolls_until_6():
    res = random.choice([1, 2, 3, 4, 5, 6])
    print(res)
    count_rolls = 1
    while res != 6:
        res = random.choice([1, 2, 3, 4, 5, 6])
        print(res)
        count_rolls = count_rolls + 1

    return count_rolls


rolls = count_rolls_until_6()
print(rolls, "rolls were needed to get 6 in a fair dice experiment")

#random dice v2
import random

def count_rolls_until_6(n):
    res = random.choice([1, 2, 3, 4, 5, 6])
    print(res)
    count_rolls = 1
    howManyTimes=0
    while howManyTimes<n:
        while res != 6:
            res = random.choice([1, 2,       3, 4, 5, 6])
            print(res)
            count_rolls = count_rolls + 1
        res=0
        howManyTimes=howManyTimes+1
    return count_rolls


rolls = count_rolls_until_6(5   )
print(rolls, "rolls were needed to get 6 in a fair dice experiment")

# Two friends want to play backgammon, but have lost the dice.
# Create a program to replace the dice. When the program is run,
# # it should roll the dice and output the result of each die.
import random
random.seed(int(input())) #please don't touch this lane

#generate the random values for every dice
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)

print(dice1)
print(dice2)
