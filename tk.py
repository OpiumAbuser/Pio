from tkinter import *


def my_action():
    print("Button clicked!")

ws = Tk()
ws.title("Button Example")
ws.geometry("300x200")

button = Button(ws, text="Click me", command=my_action)
button.pack()

ws.mainloop()