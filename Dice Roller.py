import tkinter as tk
import random
import time

while True:
    while True:
        try:
            print("What type of dice would you like to roll?")
            dice_type = int(input("D"))
            break
        except:
            print("ERROR")
            time.sleep(1)
            continue

    while True:
        try:
            print("How many dice would you like to roll?")
            num_of_rolls = int(input())
            break
        except:
            print("ERROR")
            time.sleep(1)
            continue

    total = 0
    list_of_dice = []

    for i in range(num_of_rolls):
        list_of_dice.append(random.randint(1, dice_type))
        total += list_of_dice[-1]

    if num_of_rolls != 1:
        print("The Total Value is {}".format(total))
    print("Individual Dice rolls are: {}".format(list_of_dice))

