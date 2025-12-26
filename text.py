import tkinter as tk

ws = tk.Tk()
ws.geometry("300x300")
ws.title("IT WORKS  >.<")

btn = tk.Frame(ws)
btn.pack(fill=tk.X, side=tk.BOTTOM, expand=False)

btn.rowconfigure(0, weight=1)
btn.columnconfigure(1, weight=1)
reset_button = tk.Button(btn, text="Reset")

btn.rowconfigure(0, weight=1)
btn.columnconfigure(2, weight=1)
run_button = tk.Button(btn, text="Run")

btn.rowconfigure(0, weight=1)
btn.columnconfigure(3, weight=1)
back_button = tk.Button(btn, text="Back")



reset_button.grid(row=0, column=1, sticky=tk.W+tk.E)
run_button.grid(row=0, column=2, sticky=tk.W+tk.E)
back_button.grid(row=0, column=3, sticky=tk.W+tk.E)




ws.mainloop()  