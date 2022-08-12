# libraries
import random
import os
from tkinter import *
from tkinter import messagebox
import ctypes

# UI theme colours & font
BaseBG = ("grey16",)
BG = ("grey30",)
FG = ("grey80",)
FONT = ("Calibri")

# tkinter setup
root = Tk()
root.configure(bg=BaseBG)
root.title("Random Dice Rolls!")
screensize = ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1) # read screen size using ctypes lib
windowsize = (320,480); adjustcenter = (round(screensize[0]/2-windowsize[0]/2),round(screensize[1]/2-windowsize[1]/2)) # set window size and center
root.geometry(f"{windowsize[0]}x{windowsize[1]}+{adjustcenter[0]}+{adjustcenter[1]}")  # window size and centered

# clear all changes
def clear():
    dice_side_entry.delete(0, "end");
    dice_amount_entry.delete(0, "end");
    results_label.config(text="")

# submit user input values function
def submit():
    # get user input and attach variables, otherwise error msg
    try:
        dice_side = int(dice_side_entry.get())
        dice_amount = int(dice_amount_entry.get())
    except:
        messagebox.showinfo(title="error", message="Error, value(s) invalid")
        return

    # variables setup
    dice_total = 0
    dice_rolled = []
    dice_rolled_string = ""
    if (dice_side > 100 or dice_amount > 100): # disallow input greator than 100
        messagebox.showinfo(title="error", message="Error, value(s) cannot be greator than 100")
        return

    # roll dice (random)
    for i in range(dice_amount):
        dice_rolled.append(random.randint(1, dice_side))
    for i in range(0, len(dice_rolled)):
        dice_total = dice_total + dice_rolled[i]

    # format list into string (every 10, new line)
    for i in range(len(dice_rolled) - 1):
        if i % 10 == 0:
            dice_rolled_string = str(f"{dice_rolled_string}\n{dice_rolled[i]}, ")
        else:
            dice_rolled_string = str(f"{dice_rolled_string}{dice_rolled[i]}, ")
    dice_rolled_string = str(f"{dice_rolled_string}{dice_rolled[-1]}")

    # print results to cmd (debugging)
    print("total:  ", dice_total)
    print("list:  ", dice_rolled)
    print("string: ", dice_rolled_string)

    # display results in label
    results_label.config(text=f"Rolls: {dice_rolled_string}\nTotal: {dice_total}")

# frames
topframe    = Frame(root, height=50, bg=BaseBG); topframe.pack(side=TOP, fill=X)
main_header = Label(topframe, font=(FONT, 24, "bold"), text="Random Dice Roller", bg=BaseBG, fg=FG).place(relx=0.5, rely=0.5, anchor=CENTER)

# dice type gui
global dice_side_entry
dice_side_frame   = Frame(root, height=64, bg=BaseBG); dice_side_frame.pack(side=TOP, fill=X)
dice_side_label   = Label(dice_side_frame,   font=(FONT, 16, "bold"), text="Number of Sides:", bg=BaseBG, fg=FG).place(relx=0.5, rely=0.5, anchor=S)
dice_side_entry   = Entry(dice_side_frame,   font=(FONT, 18, "bold"), justify="center", bg=BG, fg=FG); dice_side_entry.place(relx=0.5, rely=0.5, anchor=N)

# amount dice gui
global dice_amount_entry
dice_amount_frame = Frame(root, height=64, bg=BaseBG); dice_amount_frame.pack(side=TOP, fill=X)
dice_amount_label = Label(dice_amount_frame, font=(FONT, 16, "bold"), text="Number of Dice:", bg=BaseBG, fg=FG).place(relx=0.5, rely=0.5, anchor=S)
dice_amount_entry = Entry(dice_amount_frame, font=(FONT, 18, "bold"), justify="center", bg=BG, fg=FG); dice_amount_entry.place(relx=0.5, rely=0.5, anchor=N)

# submit and results gui
global response1
submit_button = Button(root, font=(FONT, 14, "bold"), text="Submit", bg="forestgreen", fg=FG, bd=3, command=submit).pack(side=TOP, pady=5)
results_label = Label(root, font=(FONT, 13, "bold"), text="", bg=BaseBG, fg=FG); results_label.pack(side=TOP, fill=X)

# keybindings
root.bind('<Return>', lambda event: submit())
root.bind('<Escape>', lambda event: clear())



root.mainloop()
