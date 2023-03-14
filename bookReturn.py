from tkinter import *
from connector import Connection
from datetime import datetime
from datetime import date
from checkdate import *

def bookReturn():
    root = Tk()
    root.geometry("800x800")

    # Background Image
    bg = PhotoImage(file = r"C:\Users\USER\Downloads\pain.png")
    background_label = Label(root, image= bg)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    frame = LabelFrame(root, text="Book Return", padx=20, pady=20, bg="#F9FBF2")
    frame.place(x = 220, y = 200)

    accession, return_date= (StringVar() for i in range(2))

    # Go back to Loans Menu
    def backToLoansMenu():
        root.destroy()
        from loansMenu import loansMenu
        loansMenu()

    # Error Message
    def error(msg):
        err = Toplevel(root)
        err.geometry("400x400")
        err.configure(background = "#d9414e")

        Label(err, text = "Error!", font = ("Mincho", 50)).place(x = 140, y = 50)
        Label(err, text = msg, font = ("Mincho", 30)).place(x = 100, y = 150)
        Button(err, text = "Back to Return Function", command = lambda: err.destroy(), font = ("Mincho", 30)).place(x = 50, y = 300)

    # Success Message
    def success():
        suc = Toplevel(root)
        suc.geometry("400x400")
        suc.configure(background = "#5ae895")

        Label(suc, text = "Success!", font = ("Mincho", 50)).place(x = 100, y = 50)
        Label(suc, text = "Book returned successfully", font = ("Mincho", 30)).place(x = 15, y = 200)
        Button(suc, text = "Back to Return Function", command = lambda: suc.destroy(), font = ("Mincho", 30)).place(x = 30, y = 300)

    # Check Function
    def check(memid, loanid, fine, input_date):
        Connection().updateBorrow(memid, 0)
        Connection().actuallyReturn(memid, loanid, fine, input_date)
        if fine > 0:
            error("Book returned\nsuccessfully\nbut has fines")
        else:
            success()
    
    # Check Inputs
    def checkInput():
        if not accession.get() or not return_date.get():
            error("Missing Input")
        elif not Connection().searchBook(accession.get()):
            error("Nonexistent Book")
        elif not Connection().getLoanDetails(accession.get()):
            error("Book not on Loan")
        elif not checkDate(return_date.get()):
            error("Invalid Date")
        else:
            returnBook()

    def returnBook():
        d = Toplevel(root)
        d.geometry("400x200")

        # Gets Book Details
        a = Connection().searchBook(accession.get())
        l = Connection().getBookDetails(a[1])

        # Get Loan Details
        loan_details = Connection().getLoanDetails(accession.get())

        # Get Member Name
        name = Connection().searchMember(loan_details[1])[1]

        temp = return_date.get().split("/")
        if len(temp[2]) == 2:
            temp[2] = "20" + temp[2]
        if len(temp[1]) == 1:
            temp[1] = "0" + temp[1]
        if len(temp[0]) == 1:
            temp[0] = "0" + temp[0]

        returnd = "/".join(temp) 

        # Calculate Fine
        input_date = datetime.datetime.strptime(returnd, "%d/%m/%Y").date()
        due_date = loan_details[3]

        fine = float((input_date - due_date).days)

        if fine < 0.0:
            fine = 0.0

        d_msg = Label(d, text = "Confirm Return Details to Be Correct")
        d_msg.grid(row = 0, column = 0)
        Label(d, text="Accession Number", bg="#F9FBF2").grid(row=1, column=0, sticky="W")
        Label(d, text=accession.get(), bg="#F9FBF2").grid(row=1, column=1, sticky="W")
        Label(d, text="Book Title", bg="#F9FBF2").grid(row=2, column=0, sticky="W")
        Label(d, text=l[1], bg="#F9FBF2").grid(row=2, column=1, sticky="W")
        Label(d, text="Membership ID", bg="#F9FBF2").grid(row=3, column=0, sticky="W")
        Label(d, text=loan_details[0], bg="#F9FBF2").grid(row=3, column=1, sticky="W")
        Label(d, text="Member Name", bg="#F9FBF2").grid(row=4, column=0, sticky="W")
        Label(d, text=name, bg="#F9FBF2").grid(row=4, column=1, sticky="W")
        Label(d, text="Return Date", bg="#F9FBF2").grid(row=5, column=0, sticky="W")
        Label(d, text=returnd, bg="#F9FBF2").grid(row=5, column=1, sticky="W")
        Label(d, text="Fine", bg="#F9FBF2").grid(row=6, column=0, sticky="W")
        Label(d, text="$" + str(fine) , bg="#F9FBF2").grid(row=6, column=1, sticky="W")

        def f(w, x, y, z):
            d.destroy()
            check(w, x, y, z)
        
        confirm = Button(d, text = "Confirm Return", command = lambda: f(loan_details[1], loan_details[0], fine, input_date))
        confirm.grid(row = 9, column = 0)
        backButton = Button(d, text = "Back to Return Function", command = lambda: d.destroy())
        backButton.grid(row = 9, column = 1)

    # Input Accession Number
    Label(frame, text="Accession Number", bg="#F9FBF2").grid(row=1, column=0, sticky="W")
    Entry(frame, textvariable = accession).grid(row=1, column=1, sticky="W")
    Label(frame, text=" ", bg="#F9FBF2").grid(row=2, column=0)

    # Input Return Date
    Label(frame, text="Return Date", bg="#F9FBF2").grid(row=3, column=0, sticky="W")
    Entry(frame, textvariable = return_date).grid(row=3, column=1, sticky="W")
    Label(frame, text=" ", bg="#F9FBF2").grid(row=4, column=0)

    # Return Book
    Button(root, text = "Return Book", command = checkInput, fg = "#8a4a22", highlightbackground = "#d4ac79", font = ("Mincho", 30)).place(x = 230, y = 400, width = 340, height = 80)
    
    # Back to Books Menu
    Button(root, text = "Back to Loans Menu", command = backToLoansMenu, fg = "#8a4a22", highlightbackground = "#d4ac79", font = ("Mincho", 30)).place(x = 230, y = 510, width = 340, height = 80)

    frame.mainloop()