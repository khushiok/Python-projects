import tkinter
from PIL import ImageTk,Image
import random


#make a window for the application
window=tkinter.Tk()
window.title("Dice roll")
window.geometry("400x400")

l0=tkinter.Label(text="\n")
l0.pack()
l1=tkinter.Label(text="hello,dice roller",fg="light green",bg="dark green",font="Helvetica 16 bold italic")
l1.pack()

#display dice images
dice=["die1.png","die2.png","die3.png" ,"die4.png","die5.png","die6.png"]
image1=ImageTk.PhotoImage(Image.open(random.choice(dice)))

#create a label for image to fit
l2=tkinter.Label(window,image=image1)
l2.pack(expand=True)

def roll_dice():
    image1=ImageTk.PhotoImage(Image.open(random.choice(dice)))

    l2.configure(image=image1)

    l2.image=image1


button=tkinter.Button(text="roll the dice",fg="yellow",bg="hot pink",command=roll_dice)
button.pack(expand=True)



window.mainloop()
