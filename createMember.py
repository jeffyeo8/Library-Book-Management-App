from tkinter import *
from tkinter import messagebox
from turtle import back
from connector import Connection

def createMember():
    root = Tk()
    root.geometry("800x800")

    # Background Image
    bg = PhotoImage(file = r"C:\Users\USER\Downloads\pain.png")
    background_label = Label(root, image= bg)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    frame = LabelFrame(root, text="Member Registration ", padx=20, pady=20, bg="#F9FBF2")
    frame.place(x = 240, y = 100)
    
    memid, name, faculty, phone, email = (StringVar() for i in range(5))

    # Input Membership ID
    Label(frame, text="Membership ID", bg="#F9FBF2").grid(row=1, column=0, sticky="W")
    Entry(frame, textvariable = memid).grid(row=1, column=1, sticky="W")
    Label(frame, text=" ", bg="#F9FBF2").grid(row=2, column=0)

    # Input Name
    Label(frame, text="Name", bg="#F9FBF2").grid(row=3, column=0, sticky="W")
    Entry(frame, textvariable = name).grid(row=3, column=1, sticky="W")
    Label(frame, text=" ", bg="#F9FBF2").grid(row=4, column=0)

    # Input Faculty
    Label(frame, text="Faculty", bg="#F9FBF2").grid(row=5, column=0, sticky="W")
    Entry(frame, textvariable = faculty).grid(row=5, column=1, sticky="W")
    Label(frame, text=" ", bg="#F9FBF2").grid(row=6, column=0)

    # Input Phone
    Label(frame, text="Phone Number", bg="#F9FBF2").grid(row=7, column=0, sticky="W")
    Entry(frame, textvariable = phone).grid(row=7, column=1, sticky="W")
    Label(frame, text=" ", bg="#F9FBF2").grid(row=8, column=0)

    # Input Email
    Label(frame, text="Email Address", bg="#F9FBF2").grid(row=9, column=0, sticky="W")
    Entry(frame, textvariable = email).grid(row=9, column=1, sticky="W")
    Label(frame, text=" ", bg="#F9FBF2").grid(row=10, column=0)

    # Create Member & Success Message
    def create(id, n, f, p, e):
        Connection().newMember(id, n, f, p, e)
        suc = Toplevel(root)
        suc.geometry("400x400")
        suc.configure(background = "#5ae895")

        Label(suc, text = "Success!", font = ("Mincho", 50)).place(x = 100, y = 50)
        Label(suc, text = "ALS Membership created", font = ("Mincho", 30)).place(x = 30, y = 200)
        Button(suc, text = "Back to Create Function", command = lambda: suc.destroy(), font = ("Mincho", 30)).place(x = 40, y = 300)

    # Error Message
    def error():
        err = Toplevel(root)
        err.geometry("400x400")
        err.configure(background = "#d9414e")

        Label(err, text = "Error!", font = ("Mincho", 50)).place(x = 140, y = 50)
        Label(err, text = "Membership already exists;\nMissing or Incomplete fields", font = ("Mincho", 30)).place(x = 15, y = 200)
        Button(err, text = "Back to Create Function", command = lambda: err.destroy(), font = ("Mincho", 30)).place(x = 40, y = 300)
    
    # Check if input is correct
    def check():
        if not memid.get() or not name.get() or not faculty.get() or not phone.get() or not email.get():
            error()
        elif name.get().isnumeric() or any(x.isdigit() for x in name.get()) or phone.get().isalpha():
            error()
        elif Connection().searchMember(memid.get()):
            error()
        else:
            create(memid.get(), name.get(), faculty.get(), phone.get(), email.get())

    # Return back to main menu
    def backToMenu():
        root.destroy()
        from main import start
        start()

    # Create Member
    Button(root, text = "Create Member", command = check, fg = "#8a4a22", highlightbackground = "#d4ac79", font = ("Mincho", 30)).place(x = 240, y = 450, width = 340, height = 80)
    
    # Back to Main Menu
    Button(root, text = "Back to Main Menu", command = backToMenu, fg = "#8a4a22", highlightbackground = "#d4ac79", font = ("Mincho", 30)).place(x = 240, y = 560, width = 340, height = 80)
    frame.mainloop()