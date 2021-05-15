import random

def diceroller(num):
    roll = random.randint(1, num)
    print("The random number chosen between 1 and",num, "=", roll)

while True:
    num = int(input("Please input the maxiumum number you want to roll: "))
    diceroller(num)
    again = input("Would you like to roll again? y/n: ")
    if again == 'y':
        continue
    if again == 'n':
        break

