from sqlite3 import connect
from tkinter import *
from tkinter import ttk
from connector import Connection

def onLoanMember():
    root = Tk()
    root.geometry("800x800")

    # Background Image
    bg = PhotoImage(file = r"C:\Users\USER\Downloads\pain.png")
    background_label = Label(root, image= bg)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    frame = LabelFrame(root, text="Books on Loan to Member", padx=20, pady=20, bg="#F9FBF2")
    frame.place(x = 230, y = 200)

    memid = StringVar() 

    # Return back to main menu
    def backToMenu():
        root.destroy()
        from  reportMenu import reportMenu
        reportMenu()

    # Error Message
    def error(msg):
        err = Toplevel(root)
        err.geometry("400x400")
        err.configure(background = "#d9414e")

        Label(err, text = "Error!", font = ("Mincho", 50)).place(x = 140, y = 50)
        Label(err, text = msg, font = ("Mincho", 30)).place(x = 120, y = 200)
        Button(err, text = "Back to Search Loans Function", command = lambda: err.destroy(), font = ("Mincho", 30)).place(x = 40, y = 300)

    def checkInput():
        if not memid.get():
            error("Missing Input")
        else:
            search()
    
    def search():
        d = Toplevel(root)
        d.geometry("800x800")

        r = Connection().memberLoans(memid.get())

        temp = list()
        for i in r:
            newi = list()
            authors = ""
            for j in range(len(i)):
                if j in [2,3,4]:
                    if i[j] != "-":
                        if not authors:
                            authors = i[j]
                        else:
                            authors = authors + ", " + i[j]
                    if j == 4:
                        newi.append(authors)
                else:
                    newi.append(i[j])
            temp.append(newi)
                

        # Scrollbar
        scroll = Scrollbar(d)
        scroll.pack(side=RIGHT, fill=Y)

        scroll = Scrollbar(d,orient='horizontal')
        scroll.pack(side= BOTTOM,fill=X)

        tab = ttk.Treeview(d,yscrollcommand=scroll.set, xscrollcommand =scroll.set)

        tab.pack()

        scroll.config(command=tab.yview)
        scroll.config(command=tab.xview)

        # Columns
        tab['columns'] = ('acc', 'title', 'authors', 'isbn', 'publisher', 'pubyear')

        # format our column
        tab.column("#0", width=0,  stretch=NO)
        tab.column("acc",anchor=CENTER, width=80)
        tab.column("title",anchor=CENTER,width=300)
        tab.column("authors",anchor=CENTER,width=100)
        tab.column("isbn",anchor=CENTER,width=100)
        tab.column("publisher",anchor=CENTER,width=150)
        tab.column("pubyear",anchor=CENTER,width=50)

        # Create Headings 
        tab.heading("#0",text="",anchor=CENTER)
        tab.heading("acc",text="Accession Number",anchor=CENTER)
        tab.heading("title",text="Title",anchor=CENTER)
        tab.heading("authors",text="Authors",anchor=CENTER)
        tab.heading("isbn",text="ISBN",anchor=CENTER)
        tab.heading("publisher",text="Publisher",anchor=CENTER)
        tab.heading("pubyear",text="Publication Year",anchor=CENTER)

        # Insert Entries
        for x in temp:
            tab.insert(parent='',index='end', text='', values = x)
        tab.pack()

        Button(d, text = "Back to Search Function", command = lambda: d.destroy(), font = ("Mincho", 30)).place(x = 225, y = 600, width = 340, height = 100)

    # Input Membership ID
    Label(frame, text="Membership ID", bg="#F9FBF2").grid(row=1, column=0, sticky="W")
    Entry(frame, textvariable = memid).grid(row=1, column=1, sticky="W")
    Label(frame, text=" ", bg="#F9FBF2").grid(row=2, column=0)

    # Search Member
    Button(root, text = "Search Book", command = checkInput, fg = "#8a4a22", highlightbackground = "#d4ac79", font = ("Mincho", 30)).place(x = 230, y = 400, width = 340, height = 80)
    
    # Back to Report Menu
    Button(root, text = "Back to Reports Menu", command = backToMenu, fg = "#8a4a22", highlightbackground = "#d4ac79", font = ("Mincho", 30)).place(x = 230, y = 510, width = 340, height = 80)
    
    frame.mainloop()