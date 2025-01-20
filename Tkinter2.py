from tkinter import *
from PIL import Image , ImageTk

window = Tk()
window.title("Image!")
window.geometry("400x400")

upload = Image.open("Gandalf_the_Grey.jpg")
image = ImageTk.PhotoImage(upload)

label = Label(window, image = image, height=350, width=300)
label.place(x=50, y=0)

window.mainloop()