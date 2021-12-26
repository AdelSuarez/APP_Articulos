import tkinter as tk

class Notification(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid(row=2, column=0, sticky=tk.NSEW, columnspan=2)
        self.bar()

    def bar(self):
        self.bar = tk.Frame(self)
        self.user = tk.Label(self, text='Developer', fg='#FFF', font='Roboto 12 bold', bg='#2979ae')
        self.user.grid(row=0, column=0)
        self.bar.grid(row=0, column=0)