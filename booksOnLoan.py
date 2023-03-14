from tkinter import *
from tkinter import ttk
from connector import Connection

def bookOnLoan():
    root = Tk()
    root.title("Books on Loan")
    root.geometry("800x800")
    
    frame = LabelFrame(root, text="Books On Loan", padx=20, pady=20, bg="#F9FBF2")

    # Return back to main menu
    def backToMenu():
        root.destroy()
        from  reportMenu import reportMenu
        reportMenu()

    l = Connection().getLoans()
    
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
    tab['columns'] = ('Accession Number', 'Title', 'Authors', 'ISBN', 'Publisher', 'Publication Year')

    # format our column
    tab.column("#0", width=0,  stretch=NO)
    tab.column("Accession Number",anchor=CENTER, width=50)
    tab.column("Title",anchor=CENTER,width=300)
    tab.column("Authors",anchor=CENTER,width=100)
    tab.column("ISBN",anchor=CENTER, width=80)
    tab.column("Publisher",anchor=CENTER,width=150)
    tab.column("Publication Year",anchor=CENTER,width=50)

    # Create Headings 
    tab.heading("#0",text="",anchor=CENTER)
    tab.heading("Accession Number",text="Accession Number",anchor=CENTER)
    tab.heading("Title",text="Title",anchor=CENTER)
    tab.heading("Authors",text="Authors",anchor=CENTER)
    tab.heading("ISBN",text="ISBN",anchor=CENTER)
    tab.heading("Publisher",text="Publisher",anchor=CENTER)
    tab.heading("Publication Year",text="Publication Year",anchor=CENTER)

    # Insert Entries
    for i in l:
        temp = list()
        for j in range(len(i)):
            if j in [3,4]:
                if i[j] != "-":
                    temp[2] = temp[2] + ", " + i[j]
            else:
                temp.append(i[j])

        tab.insert(parent='',index='end', text='', values = temp)
        tab.pack()

    # Back to Report Menu
    Button(root, text = "Back to Report Menu", command = backToMenu, fg = "black", bg = "lightgreen", font = ("Mincho", 30)).place(x = 225, y = 600, width = 340, height = 100)

    frame.mainloop()