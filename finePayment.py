from tkinter import *
from connector import Connection
from checkdate import *
from datetime import datetime
from datetime import date

def finePayment():
    root = Tk()
    root.geometry("800x800")

    # Background Image
    bg = PhotoImage(file = r"C:\Users\USER\Downloads\pain.png")
    background_label = Label(root, image= bg)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    frame = LabelFrame(root, text="Fine Payment", padx=20, pady=20, bg="#F9FBF2")
    frame.place(x = 220, y = 180)

    memid, payment_date, amt= (StringVar() for i in range(3))


    # Go back to Reservations Menu
    def backToFinesMenu():
        root.destroy()
        from finesMenu import finesMenu
        finesMenu()
    
    # Error Message
    def error(msg):
        err = Toplevel(root)
        err.geometry("400x400")
        err.configure(background = "#d9414e")

        Label(err, text = "Error!", font = ("Mincho", 50)).place(x = 140, y = 50)
        Label(err, text = msg, font = ("Mincho", 30)).place(x = 90, y = 150)
        Button(err, text = "Return to Payment Function", command = lambda: err.destroy(), font = ("Mincho", 30)).place(x = 25, y = 300)
    
    # Success Message
    def success():
        suc = Toplevel(root)
        suc.geometry("400x400")
        suc.configure(background = "#5ae895")

        Label(suc, text = "Success!", font = ("Mincho", 50)).place(x = 100, y = 50)
        Label(suc, text = "Fine Payment Successful", font = ("Mincho", 30)).place(x = 30, y = 200)
        Button(suc, text = "Return to Payment Function", command = lambda: suc.destroy(), font = ("Mincho", 30)).place(x = 15, y = 300)

    def check(paymentd):
        f = Connection().checkFine(memid.get())
        if not f:
            error("Member has no fine")
        elif float(amt.get()) != f[2]:
            error("Incorrect fine\npayment amount")
        else:
            paymentd = datetime.strptime(paymentd, "%d/%m/%Y").date()
            Connection().payFine(memid.get(), amt.get(), paymentd)
            Connection().deleteFine(memid.get())
            success()

    def checkInput():
        if not memid.get() or not payment_date.get() or not amt.get():
            error("Missing Input")
        elif not checkDate(payment_date.get()):
            error("Invalid Date")
        elif not amt.get().isnumeric() or int(amt.get()) <= 0:
            error("Invalid Amount")
        elif not Connection().searchMember(memid.get()):
            error("Invalid Member")
        elif not Connection().checkFine(memid.get()):
            error("Member has no Fine")

        else:
            payment()


    def payment():
        d = Toplevel(root)
        d.geometry("400x200")
        
        # Get Fine Details
        fine = Connection().checkFine(memid.get())

        temp = payment_date.get().split("/")
        if len(temp[2]) == 2:
            temp[2] = "20" + temp[2]
        if len(temp[1]) == 1:
            temp[1] = "0" + temp[1]

        paymentd = "/".join(temp) 

        d_msg = Label(d, text = "Confirm Fine Details to Be Correct")
        d_msg.grid(row = 0, column = 0)
        Label(d, text="Payment Due", bg="#F9FBF2").grid(row=1, column=0, sticky="W")
        Label(d, text=fine[2], bg="#F9FBF2").grid(row=1, column=1, sticky="W")
        Label(d, text="Membership ID", bg="#F9FBF2").grid(row=2, column=0, sticky="W")
        Label(d, text=memid.get(), bg="#F9FBF2").grid(row=2, column=1, sticky="W")
        Label(d, text="Payment Date", bg="#F9FBF2").grid(row=3, column=0, sticky="W")
        Label(d, text=paymentd, bg="#F9FBF2").grid(row=3, column=1, sticky="W")
        Label(d, text="Exact Fee Only", bg="#F9FBF2").grid(row=4, column=0, sticky="W")

        def f():
            d.destroy()
            check(paymentd)
        
        Button(d, text = "Confirm Payment", command = f).grid(row = 9, column = 0)
        Button(d, text = "Back to Payment Function", command = lambda: d.destroy()).grid(row = 9, column = 1)

    # Input Membership ID
    Label(frame, text="Membership ID", bg="#F9FBF2").grid(row=1, column=0, sticky="W")
    Entry(frame, textvariable = memid).grid(row=1, column=1, sticky="W")
    Label(frame, text=" ", bg="#F9FBF2").grid(row=2, column=0)

    # Input Payment Date
    Label(frame, text="Payment Date", bg="#F9FBF2").grid(row=3, column=0, sticky="W")
    Entry(frame, textvariable = payment_date).grid(row=3, column=1, sticky="W")
    Label(frame, text=" ", bg="#F9FBF2").grid(row=4, column=0)

    # Input Payment Amount
    Label(frame, text="Payment Amount", bg="#F9FBF2").grid(row=5, column=0, sticky="W")
    Entry(frame, textvariable = amt).grid(row=5, column=1, sticky="W")
    Label(frame, text=" ", bg="#F9FBF2").grid(row=6, column=0)

    # Reserve Book
    Button(root, text = "Pay Fine", command = checkInput, fg = "#8a4a22", highlightbackground = "#d4ac79", font = ("Mincho", 30)).place(x = 230, y = 415, width = 340, height = 80)
    
    # Back to Reservations Menu
    Button(root, text = "Back to Fines Menu", command = backToFinesMenu, fg = "#8a4a22", highlightbackground = "#d4ac79", font = ("Mincho", 30)).place(x = 230, y = 510, width = 340, height = 80)

    frame.mainloop()