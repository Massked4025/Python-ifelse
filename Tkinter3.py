from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("Denomination Calculator")
root.configure(bg="light gray")
root.geometry("650x400")

upload = Image.open("Gandalf_the_Grey.jpg")
upload = upload.resize((300,300))
image = ImageTk.PhotoImage(upload)

label = Label(root, image=image, bg="light gray")
label.place(x=180, y=20)

def msg():
    msgbox = messagebox.showinfo("Alert", "Do you want to count the denomination amount?")
    if msgbox == "ok":
        topwin()

button = Button(root, text="Get Started", command=msg)
button.place(x=260, y=360)

def topwin():
    top = Toplevel()
    top.title("Denomination Calculator V")
    top.configure(bg="light grey")
    top.geometry("600x350")
    label1 = Label(top, text = "Enter total amount", bg="light grey")
    entry = Entry(top)
    l1 = Label(top, text="2000", bg='light grey')
    l2 = Label(top, text="500", bg='light grey')
    l3 = Label(top, text="100", bg='light grey')
    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)
    def calculator():
        try:
            global amount
            amount = int(entry.get())
            note2000 = amount//2000
            amount %= 2000
            note500 = amount//500
            amount %= 500
            note100 = amount//100
            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)
            t1.insert(END, str(note2000))
            t2.insert(END, str(note500))
            t3.insert(END, str(note100))
        except ValueError:
            messagebox.showerror("Error", "The number is invalid")
        btn = Button(top, text='Calculate', command=calculator, bg='brown', fg='white')

# Centering Widgets in the Top Window

        label.place(x=230, y=50 )

        entry.place(x=200, y=80 )

        btn.place(x=240, y=120 )

        label1.place(x=140, y=170 )

        l1.place(x=180, y=200 )

        l2.place(x=180, y=230 )

        l3.place(x=180, y=260 )

        t1.place(x=270, y=200 )

        t2.place(x=270, y=230 )

        t3.place(x=270, y=260)

        top.mainloop()

root.mainloop()