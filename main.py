import tkinter as tk
from Manager import Manager

if __name__ == '__main__':
	print('Run app')
	root = tk.Tk()
	app = Manager(root)
	app.mainloop()
	print('Close app') 
