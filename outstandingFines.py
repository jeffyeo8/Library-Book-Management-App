from tkinter import *
from tkinter import ttk
from connector import Connection

def outstandingFines():
    root = Tk()
    root.title("Members With Outstanding Fines")
    root.geometry("800x800")
    
    # Return back to main menu
    def backToMenu():
        root.destroy()
        from  reportMenu import reportMenu
        reportMenu()

    l = Connection().getOutstandingFines()

    # Scrollbar
    scroll = Scrollbar(root)
    scroll.pack(side=RIGHT, fill=Y)

    scroll = Scrollbar(root,orient='horizontal')
    scroll.pack(side= BOTTOM,fill=X)

    tab = ttk.Treeview(root,yscrollcommand=scroll.set, xscrollcommand =scroll.set)

    tab.pack()

    scroll.config(command=tab.yview)
    scroll.config(command=tab.xview)

    # Columns
    tab['columns'] = ('memid', 'name', 'faculty', 'phone', 'email')

    # format our column
    tab.column("#0", width=0,  stretch=NO)
    tab.column("memid",anchor=CENTER, width=50)
    tab.column("name",anchor=CENTER,width=100)
    tab.column("faculty",anchor=CENTER,width=100)
    tab.column("phone",anchor=CENTER,width=100)
    tab.column("email",anchor=CENTER,width=100)

    # Create Headings 
    tab.heading("#0",text="",anchor=CENTER)
    tab.heading("memid",text="Membership ID",anchor=CENTER)
    tab.heading("name",text="Name",anchor=CENTER)
    tab.heading("faculty",text="Faculty",anchor=CENTER)
    tab.heading("phone",text="Phone Number",anchor=CENTER)
    tab.heading("email",text="Email Address",anchor=CENTER)

    # Insert Entries
    for i in l:
        tab.insert(parent='',index='end', text='', values = i)
    tab.pack()

    # Back to Report Menu
    back =Button(root, text = "Back to Report Menu", command = backToMenu, fg = "black", bg = "lightgreen", font = ("Mincho", 30))
    back.place(x = 225, y = 600, width = 340, height = 100)

    root.mainloop()