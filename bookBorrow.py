from os import access
from tkinter import *
from connector import Connection
from datetime import datetime
from datetime import timedelta

def bookBorrow():
    root = Tk()
    root.geometry("800x800")

    # Background Image
    bg = PhotoImage(file = r"C:\Users\USER\Downloads\pain.png")
    background_label = Label(root, image= bg)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    frame = LabelFrame(root, text="Book Borrow", padx=20, pady=20, bg="#F9FBF2")
    frame.place(x = 220, y = 200)

    accession, memid= (StringVar() for i in range(2))

    # Go back to Loans Menu
    def backToLoansMenu():
        root.destroy()
        from loansMenu import loansMenu
        loansMenu()

    # Error Message
    def error(msg):
        err = Toplevel(root)
        err.geometry("420x420")
        err.configure(background = "#d9414e")

        Label(err, text = "Error!", font = ("Mincho", 50)).place(x = 150, y = 50)
        Label(err, text = msg, font = ("Mincho", 30)).place(x = 60, y = 150)
        Button(err, text = "Return to Borrow Function", command = lambda: err.destroy(), font = ("Mincho", 30)).place(x = 40, y = 300)

    # Success Message
    def success():
        suc = Toplevel(root)
        suc.geometry("400x400")
        suc.configure(background = "#5ae895")

        Label(suc, text = "Success!", font = ("Mincho", 50)).place(x = 100, y = 50)
        Label(suc, text = "Book successfully Borrowed", font = ("Mincho", 30)).place(x = 15, y = 200)
        Button(suc, text = "Return to Borrow Function", command = lambda: suc.destroy(), font = ("Mincho", 30)).place(x = 30, y = 300)

    def checkInput():
        if not accession.get() or not memid.get():
            error("Missing Input")
        elif not Connection().searchBook(accession.get()):
            error("Nonexistent Book")
        elif not Connection().searchMember(memid.get()):
            error("Nonexistent Member")
        else:
            borrow()

    def check(borrow_date, duedate):
        if Connection().checkLoansBook(accession.get()):
            s = "Book currently on\nLoan until: " + Connection().getLoanDate(accession.get())[0].strftime("%d/%m/%Y")
            error(s)
        elif int(Connection().getBorrowable(memid.get())[0]) == 0:
            error("Member Loan Quota\n  Exceeded")
        elif Connection().checkOverdue(borrow_date, memid.get()):
            error("Member has Outstanding\n  Fines")
        elif Connection().checkReservationsBook(accession.get()) and not Connection().checkReservationBorrow(accession.get(), memid.get()):
            error("Book is Reserved")
        else:
            if Connection().checkReservationsExist(accession.get(), memid.get()):
                Connection().deleteReservation(accession.get(), memid.get())
                Connection().updateReservation(memid.get(), 0)

            Connection().updateBorrow(memid.get(), 1)
            Connection().actuallyBorrow(accession.get(), borrow_date, memid.get(), duedate)
            success() 


    # Confirm Loan
    def borrow():
        d = Toplevel(root)
        d.geometry("500x200")

        a = Connection().searchBook(accession.get())

        l = Connection().getBookDetails(a[1])

        date = datetime.today().strftime('%Y-%m-%d')

        due_date = (datetime.today() + timedelta(days = 14)).strftime('%Y-%m-%d')

        date2 = datetime.strptime(date, '%Y-%m-%d').strftime('%d/%m/%Y')

        due_date2 = datetime.strptime(due_date, '%Y-%m-%d').strftime('%d/%m/%Y')

        member = Connection().searchMember(memid.get())

        d_msg = Label(d, text = "Confirm Loan Details to Be Correct")
        d_msg.grid(row = 0, column = 0)
        Label(d, text="Accession Number", bg="#F9FBF2").grid(row=1, column=0, sticky="W")
        Label(d, text=accession.get(), bg="#F9FBF2").grid(row=1, column=1, sticky="W")
        Label(d, text="Book Title", bg="#F9FBF2").grid(row=2, column=0, sticky="W")
        Label(d, text=l[1], bg="#F9FBF2").grid(row=2, column=1, sticky="W")
        Label(d, text="Borrow Date", bg="#F9FBF2").grid(row=3, column=0, sticky="W")
        Label(d, text=date2, bg="#F9FBF2").grid(row=3, column=1, sticky="W")
        Label(d, text="Membership ID", bg="#F9FBF2").grid(row=4, column=0, sticky="W")
        Label(d, text=memid.get(), bg="#F9FBF2").grid(row=4, column=1, sticky="W")
        Label(d, text="Member Name", bg="#F9FBF2").grid(row=5, column=0, sticky="W")
        Label(d, text=member[1], bg="#F9FBF2").grid(row=5, column=1, sticky="W")
        Label(d, text="Due Date", bg="#F9FBF2").grid(row=6, column=0, sticky="W")
        Label(d, text=due_date2 , bg="#F9FBF2").grid(row=6, column=1, sticky="W")

        def f(x, y):
            d.destroy()
            check(x, y)
        
        confirm = Button(d, text = "Confirm Loan", command = lambda: f(date, due_date))
        confirm.grid(row = 9, column = 0)
        backButton = Button(d, text = "Back to Borrow Function", command = lambda: d.destroy())
        backButton.grid(row = 9, column = 1)

    # Input Accession Number
    Label(frame, text="Accession Number", bg="#F9FBF2").grid(row=1, column=0, sticky="W")
    Entry(frame, textvariable = accession).grid(row=1, column=1, sticky="W")
    Label(frame, text=" ", bg="#F9FBF2").grid(row=2, column=0)

    # Input Membership ID
    Label(frame, text="Membership ID", bg="#F9FBF2").grid(row=3, column=0, sticky="W")
    Entry(frame, textvariable = memid).grid(row=3, column=1, sticky="W")
    Label(frame, text=" ", bg="#F9FBF2").grid(row=4, column=0)

    # Borrow Book
    Button(root, text = "Borrow Book", command = checkInput, fg = "#8a4a22", highlightbackground = "#d4ac79", font = ("Mincho", 30)).place(x = 230, y = 400, width = 340, height = 80)
    
    # Back to Books Menu
    Button(root, text = "Back to Books Menu", command = backToLoansMenu, fg = "#8a4a22", highlightbackground = "#d4ac79", font = ("Mincho", 30)).place(x = 230, y = 510, width = 340, height = 80)

    frame.mainloop()