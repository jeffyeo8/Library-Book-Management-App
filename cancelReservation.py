from tkinter import *
from connector import Connection
from datetime import datetime
from checkdate import *

def cancelReservation():
    root = Tk()
    root.geometry("800x800")

    # Background Image
    bg = PhotoImage(file = r"C:\Users\USER\Downloads\pain.png")
    background_label = Label(root, image= bg)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    frame = LabelFrame(root, text="Cancel Reservation", padx=20, pady=20, bg="#F9FBF2")
    frame.place(x = 220, y = 180)

    accession, memid, cancel_date= (StringVar() for i in range(3))

    # Go back to Reservations Menu
    def backToReservationsMenu():
        root.destroy()
        from reserveMenu import reserveMenu
        reserveMenu()
    
    # Error Message
    def error(msg):
        err = Toplevel(root)
        err.geometry("400x400")
        err.configure(background = "#d9414e")

        Label(err, text = "Error!", font = ("Mincho", 50)).place(x = 140, y = 50)
        Label(err, text = msg, font = ("Mincho", 30)).place(x = 90, y = 175)
        Button(err, text = "Back to Cancellation Function", command = lambda: err.destroy(), font = ("Mincho", 30)).place(x = 5, y = 300)

    # Success Message
    def success():
        suc = Toplevel(root)
        suc.geometry("400x400")
        suc.configure(background = "#5ae895")

        Label(suc, text = "Success!", font = ("Mincho", 50)).place(x = 100, y = 50)
        Label(suc, text = "Reservation cancelled\nsuccessfully", font = ("Mincho", 30)).place(x = 60, y = 200)
        Button(suc, text = "Back to Cancellation Function", command = lambda: suc.destroy(), font = ("Mincho", 30)).place(x = 5, y = 300)

    def check():
        if Connection().checkReservationsExist(accession.get(), memid.get()):
            Connection().deleteReservation(accession.get(), memid.get())
            Connection().updateReservation(memid.get(), 0)
            success()
        else:
            error("Member has no\nsuch reservation")
    
    def checkInput():
        if not accession.get() or not memid.get() or not cancel_date.get():
            error("Missing Entries")
        elif not checkDate(cancel_date.get()):
            error("Invalid Date")
        elif not Connection().searchBook(accession.get()):
            error("Nonexistent Book")
        elif not Connection().searchMember(memid.get()):
            error("Nonexistant Member")
        else:
            cancel()

    # Cancel Reservation
    def cancel():
        d = Toplevel(root)
        d.geometry("600x200")

        # Gets Book Details
        a = Connection().searchBook(accession.get())
        l = Connection().getBookDetails(a[1])

        # Search Member
        name = Connection().searchMember(memid.get())[1]

        temp = cancel_date.get().split("/")
        if len(temp[2]) == 2:
            temp[2] = "20" + temp[2]
        if len(temp[1]) == 1:
            temp[1] = "0" + temp[1]

        canceld = "/".join(temp) 

        d_msg = Label(d, text = "Confirm Cancellation Details to Be Correct")
        d_msg.grid(row = 0, column = 0)
        Label(d, text="Accession Number", bg="#F9FBF2").grid(row=1, column=0, sticky="W")
        Label(d, text=accession.get(), bg="#F9FBF2").grid(row=1, column=1, sticky="W")
        Label(d, text="Book Title", bg="#F9FBF2").grid(row=2, column=0, sticky="W")
        Label(d, text=l[1], bg="#F9FBF2").grid(row=2, column=1, sticky="W")
        Label(d, text="Membership ID", bg="#F9FBF2").grid(row=3, column=0, sticky="W")
        Label(d, text=memid.get(), bg="#F9FBF2").grid(row=3, column=1, sticky="W")
        Label(d, text="Member Name", bg="#F9FBF2").grid(row=4, column=0, sticky="W")
        Label(d, text=name, bg="#F9FBF2").grid(row=4, column=1, sticky="W")
        Label(d, text="Cancellation Date", bg="#F9FBF2").grid(row=5, column=0, sticky="W")
        Label(d, text=canceld, bg="#F9FBF2").grid(row=5, column=1, sticky="W")

        def f():
            d.destroy()
            check()
        
        confirm = Button(d, text = "Confirm Cancellation", command = f)
        confirm.grid(row = 9, column = 0)
        backButton = Button(d, text = "Back to Cancellation Function", command = lambda: d.destroy())
        backButton.grid(row = 9, column = 1)

    # Input Accession Number
    Label(frame, text="Accession Number", bg="#F9FBF2").grid(row=1, column=0, sticky="W")
    Entry(frame, textvariable = accession).grid(row=1, column=1, sticky="W")
    Label(frame, text=" ", bg="#F9FBF2").grid(row=2, column=0)

    # Input Membership ID
    Label(frame, text="Membership ID", bg="#F9FBF2").grid(row=3, column=0, sticky="W")
    Entry(frame, textvariable = memid).grid(row=3, column=1, sticky="W")
    Label(frame, text=" ", bg="#F9FBF2").grid(row=4, column=0)

    # Input Cancellation Date
    Label(frame, text="Cancellation Date", bg="#F9FBF2").grid(row=5, column=0, sticky="W")
    Entry(frame, textvariable = cancel_date).grid(row=5, column=1, sticky="W")
    Label(frame, text=" ", bg="#F9FBF2").grid(row=6, column=0)

    # Reserve Book
    Button(root, text = "Cancel Reservation", command = checkInput, fg = "#8a4a22", highlightbackground = "#d4ac79", font = ("Mincho", 30)).place(x = 230, y = 415, width = 340, height = 80)
    
    # Back to Reservations Menu
    Button(root, text = "Back to Reservations Menu", command = backToReservationsMenu, fg = "#8a4a22", highlightbackground = "#d4ac79", font = ("Mincho", 25)).place(x = 230, y = 510, width = 340, height = 80)


    frame.mainloop()