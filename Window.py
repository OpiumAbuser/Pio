from tkinter import Tk, Toplevel, Button, Label, Entry

notes = []                              #this is for saving stuff


def choice_1():                         #This is the notepad
    new_win = Toplevel(ws)
    new_win.title("Notepad")
    new_win.geometry("400x300")
    Label(new_win, text="Write your mind", font=("Arial", 11)).pack(pady=10)

    entry = Entry(new_win, width=40)
    entry.pack(pady=20)

    def save():
        notetext = entry.get()
        if notetext:
            notes.append(notetext)
            entry.delete(0, "end")
            Label(new_win, text="Thought saved yippie ^..^", fg="green").pack()
    Button(new_win, text="Save Note", command=save).pack(pady=5)

def choice_2():                         #this is not a bucket this is to see yur thouzght
    new_win = Toplevel(ws)
    new_win.title("Notepad")
    new_win.geometry("400x300")
    Label(new_win, text="you wanna see your written thoughts huh? ^.^", font=("Arial", 11)).pack(pady=10)
    Label(new_win, text=notes, font=("Arial", 11)).pack(pady=10)

def choice_3():                         #and this is to kill yourself
    exit()


ws = Tk()  # main window
ws.title("Dashboard")
ws.geometry("400x300")
Label(ws, text="Choose one of these options", font=("Arial", 16)).pack(pady=20)

Button1 = Button(ws, text="Add Note", command=choice_1)
Button1.pack(pady=10)

Button2 = Button(ws, text="View Note", command=choice_2)
Button2.pack(pady=10)

Button3 = Button(ws, text="Exit Note", command=choice_3)        #so many notes WEWEWEWEWE >.<
Button3.pack(pady=10)

ws.mainloop()