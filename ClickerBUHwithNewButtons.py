from tkinter import Tk, Button, Label, Text

special_numbers = [67, 69, 187, 13, 7, 3, 6]

count = 0

def click():                            #plus click
    global count

    count += 1
    label.config(text=count)

    if count in special_numbers:
        label.config(fg="green")
    else:
        label.config(fg="yellow")
def kcilC():                            #minus click
    global count
    count -= 1
    label.config(text= count)

    if count in special_numbers:
        label.config(fg="green")
    else:
        label.config(fg="yellow")
def reset():
    global count

    if count == 67:
        count=67
        label.config(text= count)
    else:
        count = 0
        label.config(text= count)



ws = Tk()                               #window properties
ws.title("Counter")                     #name of the window
ws.geometry("300x400")                  #window size

Label(ws, text="Clicker", font=("Arial", 16)).pack(pady=20)             #what it says in the window 

label = Label(ws, text=count, font=("Arial", 30), fg="yellow")           #shows the current number
label.pack(padx=10)                                                     #anchors the number in the window and pady (y axis) space thingiii






btn = Button(ws, text="Click me", command=click)                        #thats just the submissive click me button
btn.pack(anchor="w", padx=20, pady=10)                                                 #anchors it i think idk just works like that

btn = Button(ws, text="DONT CLICK ME", command=kcilC)
btn.pack(anchor="center", padx=20, pady=10)

btn = Button(ws, text="reset >.<", command=reset)
btn.pack(anchor="e", padx=20, pady=10)


ws.mainloop(n=0)                                                        #loopie thingie for tkinter wanted to define n so i did but idk just put zero there!!!!!


import tkinter as tk

ws = tk.Tk()
ws.geometry("300x300")
ws.title("IT WORKS  >.<")

btn = tk.Frame(ws)
btn.pack(fill=tk.X, side=tk.BOTTOM, expand=False)

btn.rowconfigure(0, weight=1)
btn.columnconfigure(1, weight=1)
reset_button = tk.Button(ws, text="Reset")

btn.rowconfigure(0, weight=1)
btn.columnconfigure(2, weight=1)
run_button = tk.Button(ws, text="Run")

btn.rowconfigure(0, weight=1)
btn.columnconfigure(3, weight=1)
back_button = tk.Button(ws, text="Back")



reset_button.grid(row=0, column=1, sticky=tk.W+tk.E)
run_button.grid(row=0, column=2, sticky=tk.W+tk.E)
back_button.grid(row=0, column=3, sticky=tk.W+tk.E)




ws.mainloop()  