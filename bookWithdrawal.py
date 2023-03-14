from tkinter import *
from connector import Connection

def bookW():
    root = Tk()
    root.geometry("800x800")

    # Background Image
    bg = PhotoImage(file = r"C:\Users\USER\Downloads\pain.png")
    background_label = Label(root, image= bg)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    frame = LabelFrame(root, text="Book Acquisition", padx=20, pady=20, bg="#F9FBF2")
    frame.place(x = 220, y = 200)

    accession = StringVar()

    # Input Accession Number
    Label(frame, text="Accession Number", bg="#F9FBF2").grid(row=1, column=0, sticky="W")
    Entry(frame, textvariable = accession).grid(row=1, column=1, sticky="W")
    Label(frame, text=" ", bg="#F9FBF2").grid(row=2, column=0)

    # Go back to Books Menu
    def backToBooksMenu():
        root.destroy()
        from booksMenu import booksMenu
        booksMenu()

    # Error Message
    def error(msg):
        err = Toplevel(root)
        err.geometry("400x400")
        err.configure(background = "#d9414e")

        Label(err, text = "Error!", font = ("Mincho", 50)).place(x = 140, y = 50)
        Label(err, text = msg, font = ("Mincho", 30)).place(x = 100, y = 200)
        Button(err, text = "Return to Withdrawal Function", command = lambda: err.destroy(), font = ("Mincho", 30)).place(x = 0, y = 300)
    
    # Success Message
    def success():
        suc = Toplevel(root)
        suc.geometry("400x400")
        suc.configure(background = "#5ae895")

        Label(suc, text = "Success!", font = ("Mincho", 50)).place(x = 100, y = 50)
        Label(suc, text = "Book successfully Withdrawn", font = ("Mincho", 30)).place(x = 5, y = 200)
        Button(suc, text = "Back to Withdrawal Function", command = lambda: suc.destroy(), font = ("Mincho", 30)).place(x = 10, y = 300)

    def checkInput():
        if not accession.get():
            error("Missing Input")
        else:
            check()
    
    # Withdraw Books
    def withdraw(a):
        d = Toplevel(root)
        d.geometry("500x300")

        def f(x, y):
            d.destroy()
            z = Connection().checkNumBooks(y)
            Connection().withdrawBook(x, y, z)
            success()

        l = Connection().getBookDetails(a[1])

        d_msg = Label(d, text = "Please Confirm Details to Be Correct")
        d_msg.grid(row = 0, column = 0)
        Label(d, text="Accession Number", bg="#F9FBF2").grid(row=1, column=0, sticky="W")
        Label(d, text=accession.get(), bg="#F9FBF2").grid(row=1, column=1, sticky="W")
        Label(d, text="Title", bg="#F9FBF2").grid(row=2, column=0, sticky="W")
        Label(d, text=l[1], bg="#F9FBF2").grid(row=2, column=1, sticky="W")
        Label(d, text="Author 1", bg="#F9FBF2").grid(row=3, column=0, sticky="W")
        Label(d, text=l[2], bg="#F9FBF2").grid(row=3, column=1, sticky="W")
        Label(d, text="Author 2", bg="#F9FBF2").grid(row=4, column=0, sticky="W")
        Label(d, text=l[3], bg="#F9FBF2").grid(row=4, column=1, sticky="W")
        Label(d, text="Author 3", bg="#F9FBF2").grid(row=5, column=0, sticky="W")
        Label(d, text=l[4], bg="#F9FBF2").grid(row=5, column=1, sticky="W")
        Label(d, text="ISBN", bg="#F9FBF2").grid(row=6, column=0, sticky="W")
        Label(d, text=l[0], bg="#F9FBF2").grid(row=6, column=1, sticky="W")
        Label(d, text="Publisher", bg="#F9FBF2").grid(row=7, column=0, sticky="W")
        Label(d, text=l[5], bg="#F9FBF2").grid(row=7, column=1, sticky="W")
        Label(d, text="Year", bg="#F9FBF2").grid(row=8, column=0, sticky="W")
        Label(d, text=l[6], bg="#F9FBF2").grid(row=8, column=1, sticky="W")
        
        confirm = Button(d, text = "Confirm", command = lambda: f(accession.get(), l[0]))
        confirm.grid(row = 9, column = 0)
        backButton = Button(d, text = "Back to Delete Function", command = lambda: d.destroy())
        backButton.grid(row = 9, column = 1)
    
    # Check Function
    def check():
        res = Connection().searchBook(accession.get())
        if res:
            if Connection().checkLoansBook(accession.get()):
                error("Book is currently\non Loan.")
            elif Connection().checkReservationsBook(accession.get()):
                error("Book is currently\nReserved")
            else:
                withdraw(res)
        else:
            error("Book does not exist")

    # Withdraw Book
    Button(root, text = "Withdraw Book", command = checkInput, fg = "#8a4a22", highlightbackground = "#d4ac79", font = ("Mincho", 30)).place(x = 230, y = 400, width = 340, height = 80)
    
    # Back to Books Menu
    Button(root, text = "Back to Books Menu", command = backToBooksMenu, fg = "#8a4a22", highlightbackground = "#d4ac79", font = ("Mincho", 30)).place(x = 230, y = 510, width = 340, height = 80)

    frame.mainloop()