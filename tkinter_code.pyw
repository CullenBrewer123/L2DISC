import random
import os
from tkinter import *
import ctypes

# UI theme colours & other
BaseBG = ("grey16",)
BG = ("grey30",)
FG = ("grey80",)
FONT = ("Calibri")

root = Tk()
root.configure(bg=BaseBG)
root.title("Dice Roller")
screensize = ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1) # read screen size using ctypes lib
windowsize = (300,400); adjustcenter = (round(screensize[0]/2-windowsize[0]/2),round(screensize[1]/2-windowsize[1]/2)) # set window size and center
root.geometry(f"{windowsize[0]}x{windowsize[1]}+{adjustcenter[0]}+{adjustcenter[1]}")  # window size and centered


main_header = Label(font=(FONT, 24, "bold"), text="This is a Simple to Use Dice Roller").grid(row=1, column=2)

dice_type_label = Label(font=(FONT, 18, "bold"), text="Dice Type:").grid(row=3, column=2) # This is the label for the dice type
dice_type_input_variable = IntVar() # Similar to the other code it has an input box where the user can type a number
dice_type_input = Entry(font=(FONT, 18, "bold"))
dice_type_input.grid(row=4, column=2) # As you can see throughout the code every visual aspect in the Tkinter program is gridded. This keeps it tidy

number_of_dice_label = Label(font=(FONT, 18, "bold"), text="Number of Dice:").grid(row=6, column=2) # Same type of label as before only for the number of dice
dice_number_input_variable = IntVar() # Same type of input box only this is for the number of dice. Numbers only
dice_number_input = Entry(font=(FONT, 18, "bold"))
dice_number_input.grid(row=7, column=2)

#def clear():

def submit(): # This is the main chunk of code that gets the users input and randomizies it. Similar to the other code with some added lines related to Tkinter
    total = 0
    list_of_dice = []
    dice_type = int(dice_type_input.get())
    num_of_dice = int(dice_number_input.get())
    if (dice_type > 100 or num_of_dice > 100):
        os.system("msg %username% Error; Values cannot be above 100") # This is an error line that is used in the same way as the other code, only it is displayed using os
        return
    for i in range(num_of_dice):
        list_of_dice.append(random.randint(1, dice_type))
    for i in range(0, len(list_of_dice)):
        total = total + list_of_dice[i]

    print("total:", total) # These two print statements are the results of the randomizations
    print("list:", list_of_dice)
    try:
        r1.destroy; r2.destroy;
    except: pass
    response1.configure(text="List: {}".format(list_of_dice)).grid(row=11, column=2) # These two labels actually show the results in the window below the submit button
    response2.configure(text="Total: {}".format(total)).grid(row=12, column=2)


response1 = Label(); response1.grid(row=11, column=2)
response2 = Label(); response2.grid(row=12, column=2)

root.bind('<Return>', lambda event: submit()) # This is a small line of code that allows the user to use the enter/return key to move from one input to another quickly
root.bind('<Escape>', lambda event: root.destroy())

submit_button = Button(text="Submit", command=submit).grid(row=10, column=2) # This is the submit button and it calls the function when clicked

root.mainloop()
