import random

dice_type = int(input("What type of dice would you like to roll? "))
num_of_dice = int(input("How many dice would you like to roll? "))
total = 0
list_of_dice = []

for i in range(num_of_dice):
    list_of_dice.append(random.randint(1, dice_type))
    total += list_of_dice[-1]

print(f"The Total Value is {total}")
print(f"Individual Dice rolls are: {list_of_dice}")
