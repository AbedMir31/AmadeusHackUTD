import tkinter as tk

w1 = tk.Tk()
w1.title("Vibe Check")
b1 = tk.Button(w1, text="Vibin'", width=25, command=w1.destroy)
b1.pack()
w1.mainloop()
