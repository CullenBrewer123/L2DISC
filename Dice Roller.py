import random

dicetype = int(input("What type of dice would you like to roll? "))
numofdice = int(input("How many dice would you like to roll? "))
total = 0
listofdice = []
for i in range(numofdice):
    listofdice.append(random.randint(1,dicetype))
    total += listofdice[-1]



print(f"The Total Value is ", total)
print("Individual Dice rolls are:{}".format(listofdice))
