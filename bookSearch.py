from tkinter import *
from tkinter import ttk
from connector import Connection

def bookSearch():
    root = Tk()
    root.geometry("800x800")

    # Background Image
    bg = PhotoImage(file = r"C:\Users\USER\Downloads\pain.png")
    background_label = Label(root, image= bg)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    frame = LabelFrame(root, text="Book Search", padx=20, pady=20, bg="#F9FBF2")
    frame.place(x = 220, y = 120)
    
    title, authors, isbn, publisher, pubyear = (StringVar() for i in range(5))

    # Return back to report menu
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
        Button(err, text = "Return to Search Function", command = lambda: err.destroy(), font = ("Mincho", 30)).place(x = 25, y = 300)
    
    def checkInput():
        l = [title.get(), authors.get(), isbn.get(), publisher.get(), pubyear.get()]
        if not any(l):
            error("Missing Input")
        elif sum(1 for i in l if i) > 1:
            error("Too Many Inputs")
        else:
            search()

    # Search Function
    def search():
        d = Toplevel(root)
        d.geometry("800x800")

        l = [title.get(), authors.get(), isbn.get(), publisher.get(), pubyear.get()]
        index = 0
        x = ""
        for i in l:
            if i:
                index = l.index(i)
                if index == 1:
                    s = i.split(",")
                    x = s
                    break
                x = i
                break
        

        r = Connection().search(index, x)

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
        tab['columns'] = ('ISBN', 'Title', 'Authors', 'Publisher', 'Publication Year')

        # format our column
        tab.column("#0", width=0,  stretch=NO)
        tab.column("ISBN",anchor=CENTER, width=80)
        tab.column("Title",anchor=CENTER,width=300)
        tab.column("Authors",anchor=CENTER,width=500)
        tab.column("Publisher",anchor=CENTER,width=150)
        tab.column("Publication Year",anchor=CENTER,width=50)

        # Create Headings 
        tab.heading("#0",text="",anchor=CENTER)
        tab.heading("ISBN",text="ISBN",anchor=CENTER)
        tab.heading("Title",text="Title",anchor=CENTER)
        tab.heading("Authors",text="Authors",anchor=CENTER)
        tab.heading("Publisher",text="Publisher",anchor=CENTER)
        tab.heading("Publication Year",text="Publication Year",anchor=CENTER)

        # Insert Entries
        for i in r:
            temp = list()
            for j in range(len(i)):
                if j in [3,4]:
                    if i[j] != "-":
                        temp[2] = temp[2] + ", " + i[j]
                else:
                    temp.append(i[j])

            tab.insert(parent='',index='end', text='', values = temp)
            tab.pack()

        Button(d, text = "Back to Search Function", command = lambda: d.destroy(), font = ("Mincho", 30)).place(x = 225, y = 600, width = 340, height = 100)
            


    # Input Title
    Label(frame, text="Title", bg="#F9FBF2").grid(row=1, column=0, sticky="W")
    Entry(frame, textvariable = title).grid(row=1, column=1, sticky="W")
    Label(frame, text=" ", bg="#F9FBF2").grid(row=2, column=0)

    # Input Authors
    Label(frame, text="Authors", bg="#F9FBF2").grid(row=3, column=0, sticky="W")
    Entry(frame, textvariable = authors).grid(row=3, column=1, sticky="W")
    Label(frame, text=" ", bg="#F9FBF2").grid(row=4, column=0)

    # Input ISBN
    Label(frame, text="ISBN", bg="#F9FBF2").grid(row=5, column=0, sticky="W")
    Entry(frame, textvariable = isbn).grid(row=5, column=1, sticky="W")
    Label(frame, text=" ", bg="#F9FBF2").grid(row=6, column=0)

    # Input Publisher
    Label(frame, text="Publisher", bg="#F9FBF2").grid(row=7, column=0, sticky="W")
    Entry(frame, textvariable = publisher).grid(row=7, column=1, sticky="W")
    Label(frame, text=" ", bg="#F9FBF2").grid(row=8, column=0)

    # Input Publication Year
    Label(frame, text="Publication Year", bg="#F9FBF2").grid(row=9, column=0, sticky="W")
    Entry(frame, textvariable = pubyear).grid(row=9, column=1, sticky="W")
    Label(frame, text=" ", bg="#F9FBF2").grid(row=10, column=0)

    # Search Book
    Button(root, text = "Search Book", command = checkInput, fg = "#8a4a22", highlightbackground = "#d4ac79", font = ("Mincho", 30)).place(x = 225, y = 460, width = 340, height = 80)
    
    # Back to Report Menu
    Button(root, text = "Back to Report Menu", command = backToMenu, fg = "#8a4a22", highlightbackground = "#d4ac79", font = ("Mincho", 30)).place(x = 225, y = 560, width = 340, height = 80)

    frame.mainloop()
