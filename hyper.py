from Tkinter import *
import webbrowser

def linkadd(self):
    webbrowser.open_new(r"http://www.google.com")

root = Tk()

def l():
	link = Label(root, text="Google Hyperlink", fg="blue", cursor="hand2")
	link.pack()
	link.bind("<Button-1>", linkadd)
	root.mainloop()


