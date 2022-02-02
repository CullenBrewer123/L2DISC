import random
import os
from tkinter import *

root = Tk()
root.title("Dice Roller")

main_header = Label(text="This is a Simple to Use Dice Roller").grid(row=1, column=2)

dice_type_label = Label(text="Dice Type:").grid(row=3, column=2) #This is the label for the dice type.#
dice_type_input_variable = IntVar() #Similar to the other code it has an input box where the user can type a number.#
dice_type_input = Entry()
dice_type_input.grid(row=4, column=2) #As you can see throughout the code every visual aspect in the Tkinter program is gridded. This keeps it tidy.#

number_of_dice_label = Label(text="Number of Dice:").grid(row=6, column=2) #Same type of label as before only for the number of dice.#
dice_number_input_variable = IntVar() #Same type of input box only this is for the number of dice. Numbers only.#
dice_number_input = Entry()
dice_number_input.grid(row=7, column=2)


def submit(): #This is the main chunk of code that gets the users input and randomizies it. Similar to the other code with some added lines related to Tkinter.#
    total = 0
    list_of_dice = []
    dice_type = int(dice_type_input.get())
    num_of_dice = int(dice_number_input.get())
    if (dice_type > 100 or num_of_dice > 100):
        os.system("msg %username% Error; Values cannot be above 100") #This is an error line that is used in the same way as the other code, only it is displayed using os.#
        return
    for i in range(num_of_dice):
        list_of_dice.append(random.randint(1, dice_type))
    for i in range(0, len(list_of_dice)):
        total = total + list_of_dice[i]

    print("total:", total) #These two print statements are the results of the randomizations.# 
    print("list:", list_of_dice)
    Label(text="List: {}".format(list_of_dice)).grid(row=11, column=2) #These two labels actually show the results in the window below the submit button.#
    Label(text="Total: {}".format(total)).grid(row=12, column=2)


root.bind('<Return>', lambda event: submit()) #This is a small line of code that allows the user to use the enter/return key to move from one input to another quickly.#
root.bind('<Escape>', lambda event: root.destroy()) #
submit_button = Button(text="Submit", command=submit).grid(row=10, column=2) #This is the submit button and it calls the function when clicked.#

root.mainloop()
