import tkinter as tk

window = tk.Tk()
window.title("Welcome to the page")
window.geometry("300x400")

label = tk.Label(text="Label", fg="white", bg='black')
button = tk.Button(text="Click me, please", fg='white', bg='red')
entry = tk.Entry(fg='blue', bg='green', width=50)

label.pack()
button.pack()
entry.pack()

frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=5)
label = tk.Label(master=frame, text="Hi")
frame.pack()
label.pack()

textbox= tk.Text(fg="black", bg="white")
textbox.pack()

window.mainloop()