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

topframe = Frame(root, height=64, bg=BaseBG); topframe.pack(side=TOP, fill=X)
main_header = Label(topframe, font=(FONT, 24, "bold"), text="Random Dice Roller", bg=BaseBG).place(relx=0.5, rely=0.5, anchor=CENTER)

dicetypeframe = Frame(root, height=64, bg=BaseBG); dicetypeframe.pack(side=TOP, fill=X)
dice_type_label = Label(dicetypeframe, font=(FONT, 18, "bold"), text="Dice Type:", bg=BaseBG).place(relx=0.5, rely=0.5, anchor=S)
dice_type_input_variable = IntVar()
dice_type_input = Entry(dicetypeframe, font=(FONT, 18, "bold"), bg=BaseBG); dice_type_input.place(relx=0.5, rely=0.5, anchor=N)

diceamountframe = Frame(root, height=64, bg=BaseBG); diceamountframe.pack(side=TOP, fill=X)
dice_number_label = Label(diceamountframe, font=(FONT, 18, "bold"), text="Number of Dice:", bg=BaseBG).place(relx=0.5, rely=0.5, anchor=S)
dice_number_input_variable = IntVar()
dice_number_input = Entry(diceamountframe, font=(FONT, 18, "bold"), bg=BaseBG); dice_number_input.place(relx=0.5, rely=0.5, anchor=N)

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
    diceindividual = ""
    for i in range(len(list_of_dice)-1):
        diceindividual = str(f"{diceindividual}{list_of_dice[i]}, ")
    diceindividual = str(f"{diceindividual}{list_of_dice[-1]}")
    print(diceindividual)

    print("total:", total) # These print statements are the results of the randomisations
    print("list:", list_of_dice)
    print("dice printout", diceindividual)


    response1.config(responseframe, text="List: {}".format(list_of_dice))
    response2.config(responseframe, text="Total: {}".format(total))

responseframe = Frame(root, height=64, bg=BaseBG); responseframe.pack(side=TOP, fill=X)
global response1, response2
response1 = Label(responseframe, font=(FONT, 14, "bold"), text=""); response1.place(relx=0.5, rely=0.5, anchor=S)
response2 = Label(responseframe, font=(FONT, 14, "bold"), text=""); response2.place(relx=0.5, rely=0.5, anchor=N)

root.bind('<Return>', lambda event: submit())
root.bind('<Escape>', lambda event: root.destroy())

#bottomframe = Frame(root, height=64, bg=BaseBG); topframe.pack(side=TOP, fill=X)
submit_button = Button(root, text="Submit", command=submit).pack(side=TOP) # This is the submit button and it calls the function when clicked

root.mainloop()
