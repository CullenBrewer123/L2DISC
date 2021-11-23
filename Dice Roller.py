import random
import time

while True:
    while True: #This while True statement dictates the type of dice rolled.# 
        try:
            print("What type of dice would you like to roll?") #These next three lines are for the input of the user, an input statement.#
            dice_type = int(input("D"))
            break
        except:
            print("ERROR") #This is for when the user inputs anything other than a number. It comes up with an error message.#
            time.sleep(1)
            continue

    while True: #This while True statement dictates the number of dice rolled.#
        try:
            print("How many dice would you like to roll?") #This is the same type of input statement as the last one.#
            num_of_rolls = int(input())
            break
        except:
            print("ERROR") #Same error message as before.#
            time.sleep(1)
            continue

    total = 0
    list_of_dice = [] #To the user this will display indiviual results for the dice roll.#

    for i in range(num_of_rolls): #These next three lines are the randomization for the user inputs.#
        list_of_dice.append(random.randint(1, dice_type))
        total += list_of_dice[-1]

    if num_of_rolls != 1:
        print("The Total Value is {}".format(total)) #These two print statements display the results of the randomization.# 
    print("Individual Dice rolls are: {}".format(list_of_dice))
