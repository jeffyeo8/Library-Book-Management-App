from tkinter import *
from connector import Connection

def deleteMember():
    root = Tk()
    root.geometry("800x800")

    # Background Image
    bg = PhotoImage(file = r"C:\Users\USER\Downloads\pain.png")
    background_label = Label(root, image= bg)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    frame = LabelFrame(root, text="Membership Deletion ", padx=20, pady=20, bg="#F9FBF2")
    frame.place(x = 230, y = 200)
    
    memid = StringVar() 

    # Input Membership ID
    Label(frame, text="Membership ID", bg="#F9FBF2").grid(row=1, column=0, sticky="W")
    Entry(frame, textvariable = memid).grid(row=1, column=1, sticky="W")
    Label(frame, text=" ", bg="#F9FBF2").grid(row=2, column=0)

    # Success Message
    def success():
        suc = Toplevel(root)
        suc.geometry("400x400")
        suc.configure(background = "#5ae895")

        Label(suc, text = "Success!", font = ("Mincho", 50)).place(x = 100, y = 50)
        Label(suc, text = "ALS Membership Deleted.", font = ("Mincho", 30)).place(x = 30, y = 200)
        Button(suc, text = "Back to Delete Function", command = lambda: suc.destroy(), font = ("Mincho", 30)).place(x = 40, y = 300)

    # Error Message
    def error(msg):
        err = Toplevel(root)
        err.geometry("400x400")
        err.configure(background = "#d9414e")

        Label(err, text = "Error!", font = ("Mincho", 50)).place(x = 140, y = 50)
        Label(err, text = msg, font = ("Mincho", 30)).place(x = 60, y = 150)
        Button(err, text = "Back to Delete Function", command = lambda: err.destroy(), font = ("Mincho", 30)).place(x = 40, y = 300)
        
    def delete(l):
        d = Toplevel(root)
        d.geometry("400x200")

        def f(v):
            d.destroy()
            Connection().deleteMember(v)
            success()

        d_msg = Label(d, text = "Please Confirm Details to Be Correct")
        d_msg.grid(row = 0, column = 0)
        Label(d, text="Membership ID", bg="#F9FBF2").grid(row=1, column=0, sticky="W")
        Label(d, text=l[0], bg="#F9FBF2").grid(row=1, column=1, sticky="W")
        Label(d, text="Name", bg="#F9FBF2").grid(row=2, column=0, sticky="W")
        Label(d, text=l[1], bg="#F9FBF2").grid(row=2, column=1, sticky="W")
        Label(d, text="Faculty", bg="#F9FBF2").grid(row=3, column=0, sticky="W")
        Label(d, text=l[2], bg="#F9FBF2").grid(row=3, column=1, sticky="W")
        Label(d, text="Phone Number", bg="#F9FBF2").grid(row=4, column=0, sticky="W")
        Label(d, text=l[3], bg="#F9FBF2").grid(row=4, column=1, sticky="W")
        Label(d, text="Email Address", bg="#F9FBF2").grid(row=5, column=0, sticky="W")
        Label(d, text=l[4], bg="#F9FBF2").grid(row=5, column=1, sticky="W")
        
        confirm = Button(d, text = "Confirm Deletion", command = lambda: f(l[0]))
        confirm.grid(row = 6, column = 0)
        backButton = Button(d, text = "Back to Delete Function", command = lambda: d.destroy())
        backButton.grid(row = 6, column = 1)


    def check():
        res = Connection().searchMember(memid.get())
        if res:
            if Connection().checkFine(memid.get()) or Connection().checkReservation(memid.get()) or Connection().checkLoans(memid.get()):
                error("Member has loans,\nreservations or\noutstanding fines")
            else:
                delete(res)
        else:
            error("Nonexistent Member")

    # Return back to main menu
    def backToMenu():
        root.destroy()
        from main import start
        start()

    # Delete Member
    Button(root, text = "Delete Member", command = check, fg = "#8a4a22", highlightbackground = "#d4ac79", font = ("Mincho", 30)).place(x = 230, y = 400, width = 340, height = 80)
    
    # Back to Main Menu
    Button(root, text = "Back to Main Menu", command = backToMenu, fg = "#8a4a22", highlightbackground = "#d4ac79", font = ("Mincho", 30)).place(x = 230, y = 510, width = 340, height = 80)

    frame.mainloop()