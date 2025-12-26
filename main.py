from tkinter import Tk, Button, Label, messagebox, simpledialog
ws = Tk()

print("=== My Dashboard App ===")
print("1. Add note")
print("2. View notes")
print("3. Exit")


while True:


    def choice1():
        print("You choose a note")
        ws.title('Note')
        ws.geometry('400x300')
    title = messagebox.showinfo("Title", "Choose the title of your note: ")         #ima change that later too
    content = messagebox.showinfo("Title", "Enter the chontent of the note: ")      #ima change that later
        

    Button = Button(ws, text="1", command=choice1)
    Button.pack()  
    

