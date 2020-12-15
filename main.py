from tkinter import *
import random



root = Tk()
root.title('Random Number Generator')
root.geometry("550x380")
root.resizable(width=False, height=False)


def rando():
    txt = E1.get()
    s, r = txt.split(",")
    num_1 = int(s)
    num_2 = int(r)
    out = random.randrange(num_1, num_2)
    updateDisplay(out)


def updateDisplay(myString):
    god.set(myString)

canvas = Canvas(root, width = 330, height = 70)      
canvas.pack()      
img = PhotoImage(file="2.png")      
canvas.create_image(20,20, anchor=NW, image=img)  

label1 = Label(root, text="@_@ HERE @_@", font=("Helvetica", 24))
label1.pack(pady=20)


E1 = Entry(root, width=22)
E1.insert(0, '1,2')
E1.pack()


win_button = Button(root, text="Touch Me!!!",
                    font=("Helvetica", 24), command=rando)
win_button.pack(pady=20)

god = StringVar()
label2 = Label(root, textvariable=god, font=("Helvetica", 38))
label2.pack(pady=20)

root.mainloop()
