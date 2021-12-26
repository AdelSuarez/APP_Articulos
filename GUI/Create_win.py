import tkinter as tk


class Create_win(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid(row=1, column=1, sticky=tk.NSEW)

    def create(self):
        self.create_frame = tk.Frame(self)

        self

        self.create_frame.grid(row=0, column=0)