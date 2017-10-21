from Tkinter import *

root=Tk()


def about():
    photo = PhotoImage(file="logo.gif")
    label1 = Label(root,image=photo)
    label1.grid()
    root.mainloop()

print about()


