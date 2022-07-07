import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

class StartFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        test = tk.Label(text="test").pack()

class NextFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        test = tk.Label(text="test").pack()

app = App()
frame = MainFrame(app)
app.mainloop()