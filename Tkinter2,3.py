from tkinter import *

window = Tk()
window.title("Tkinter")
window.geometry("200x300")

def topwin():
    top=Toplevel()
    top.title("Top window")
    top.geometry("200x200")
    label=Label(top, text="This is the top level window")
    label.pack()
    top.mainloop()

button = Button(window, text = "Click me", command=topwin)
button.pack()
window.mainloop()