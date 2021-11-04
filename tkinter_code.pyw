import random
from tkinter import *

def submit():
    total = 0
    list_of_dice = []
    dice_type = dice_type_input.get()
    num_of_dice = dice_number_input.get()
    for i in range(int(num_of_dice)):
        list_of_dice.append(random.randint(1, int(dice_type)))
    for g in range(0, len(list_of_dice)):
        total = total + list_of_dice[g]

    print("total:", total)
    print("list:", list_of_dice)

root = Tk()
root.title("Dice Roller")

main_header = Label(text="This is a Simple to Use Dice Roller").grid(row=1, column=2)

dice_type_label = Label(text="Dice Type:").grid(row=3, column=2)
dice_type_input_variable = IntVar()
dice_type_input = Entry()
dice_type_input.grid(row=4, column=2)

number_of_dice_label = Label(text="Number of Dice:").grid(row=6, column=2)
dice_number_input_variable = IntVar()
dice_number_input = Entry()
dice_number_input.grid(row=7, column=2)
root.bind(('<Return>'), lambda event:submit())

submit_button = Button(text="ROLL", command=submit).grid(row=10, column=2)

root.mainloop()
