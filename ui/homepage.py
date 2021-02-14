from tkinter import *
from tkinter import ttk
#sets up root element
root = Tk()
root.title("Finance Tracker")

#sets up mainframe element within root
mainframe = ttk.Frame(root, padding=(3, 12))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

accounts = ["checking", "savings", "investment"]
accountsvar = StringVar(value=accounts)
l = Listbox(mainframe, listvariable=accountsvar)
accounts.append("peach")
accountsvar.set(accounts)


root.mainloop()