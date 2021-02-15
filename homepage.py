from tkinter import *
from tkinter import ttk
import budget


#definition of functions for ui
#problem, this should be what happens when the button is clicked, and I need it to run "name = newCat(name)" which needs to be set as a golabl variable?
#tkinter is not going to do anything with whatever is returned from the function.
#if the category object is placed into the list we can use the list to access it?
catList = []
catNameList = []
# use catNameList to populate menu
def newCat(name):
    #returns new category
    print(name.get())
    res = budget.Category(name)
    catList.append(res)
    catNameList.append(res.name)
    return res


#sets up root element
root = Tk()
root.title("Finance Tracker")

#sets up mainframe element within root
mainframe = ttk.Frame(root, padding=(3, 12))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="category name:").grid(column=1, row=1, sticky=W)
cat = StringVar()
cat_entry = ttk.Entry(mainframe, width=7, textvariable=cat)
cat_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Button(mainframe, text="Create Category", command=newCat(cat)).grid(column=3, row=3, sticky=W)

#Need a table to display transactions/ledger, but the problem is that tkinter doesn't include a table widget or anything really like it.

# ACCOUNTS LIST
accounts = ["checking", "savings", "investment"]
accountsvar = StringVar(value=catNameList)
l = Listbox(mainframe, listvariable=accountsvar)
l.grid(column=1, row=1)

root.mainloop()