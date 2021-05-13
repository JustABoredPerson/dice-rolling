import random

def diceroller(num):
    roll = random.randint(1, num)
    print("The random number between 1 and",num, "=", roll)

num = int(input("Please input the maxiumum number you want to roll: "))
diceroller(num)