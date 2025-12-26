import tkinter as tk

ws = tk.Tk()
ws.geometry("300x300")
ws.title("IT WORKS  >.<")

button_frame = tk.Frame(ws)
button_frame.pack(fill=tk.X, side=tk.BOTTOM, expand=False)

button_frame.rowconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
reset_button = tk.Button(button_frame, text="Reset")

button_frame.rowconfigure(0, weight=1)
button_frame.columnconfigure(2, weight=1)
run_button = tk.Button(button_frame, text="Run")

button_frame.rowconfigure(0, weight=1)
button_frame.columnconfigure(3, weight=1)
back_button = tk.Button(button_frame, text="Back")



reset_button.grid(row=0, column=1, sticky=tk.W+tk.E)
run_button.grid(row=0, column=2, sticky=tk.W+tk.E)
back_button.grid(row=0, column=3, sticky=tk.W+tk.E)




ws.mainloop()   



# from tkinter import Tk, Button, Label

# ws = Tk()
# ws.geometry("300x300")
# ws.title("Buttons")
# Label(ws, text="How buttons work", font=("arial", 16)).pack(pady=20)

# btn = Button(ws, text="Button 1")
# btn.pack(grid="2x2")

# ws.mainloop(n=0)