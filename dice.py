# bias dice
import random
from tkinter import *
root = Tk()
root.geometry("700x450")
l1 = Label(root, font=("times", 200))

# repeated instances of \u2685 has resulted more probability of getting 6 in this die


def roll():
    number = ['\u2680', '\u2681', '\u2682', '\u2684',
              '\u2685', '\u2685', '\u2685', '\u2685']
    l1.config(text=f'{random.choice(number)}')
    l1.pack()


b1 = Button(root, text="ROLL", width=10, command=roll)
b1.place(x=350, y=0)
root.mainloop()
