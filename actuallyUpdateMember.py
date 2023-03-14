from tkinter import *
from connector import Connection

def actuallyUpdateMember(memid):
    root = Tk()
    root.geometry("800x800")

    # Background Image
    bg = PhotoImage(file = r"C:\Users\USER\Downloads\pain.png")
    background_label = Label(root, image= bg)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    frame = LabelFrame(root, text="Membership Update ", padx=20, pady=20, bg="#F9FBF2")
    frame.place(x = 240, y = 100)
    
    name, faculty, phone, email = (StringVar() for i in range(4))

    Label(frame, text="Membership ID", bg="#F9FBF2").grid(row=1, column=0, sticky="W")
    Label(frame, text=memid, bg="#F9FBF2").grid(row=1, column=1, sticky="W")

    # Input Name
    Label(frame, text="Name", bg="#F9FBF2").grid(row=2, column=0, sticky="W")
    Entry(frame, textvariable = name).grid(row=2, column=1, sticky="W")
    Label(frame, text=" ", bg="#F9FBF2").grid(row=3, column=0)

    # Input Faculty
    Label(frame, text="Faculty", bg="#F9FBF2").grid(row=4, column=0, sticky="W")
    Entry(frame, textvariable = faculty).grid(row=4, column=1, sticky="W")
    Label(frame, text=" ", bg="#F9FBF2").grid(row=5, column=0)

    # Input Phone
    Label(frame, text="Phone Number", bg="#F9FBF2").grid(row=6, column=0, sticky="W")
    Entry(frame, textvariable = phone).grid(row=6, column=1, sticky="W")
    Label(frame, text=" ", bg="#F9FBF2").grid(row=7, column=0)

    # Input Email
    Label(frame, text="Email Address", bg="#F9FBF2").grid(row=8, column=0, sticky="W")
    Entry(frame, textvariable = email).grid(row=8, column=1, sticky="W")
    Label(frame, text=" ", bg="#F9FBF2").grid(row=9, column=0)

    # Go back to Membership Menu
    def backToMemMenu():
        from membershipMenu import membershipMenu
        root.destroy()
        membershipMenu()
    
    # Go to Create Member Page
    def goToCreate():
        from createMember import createMember
        root.destroy()
        createMember()

    # Error Message
    def error(msg):
        err = Toplevel(root)
        err.geometry("400x400")
        err.configure(background = "#d9414e")

        Label(err, text = "Error!", font = ("Mincho", 50)).place(x = 140, y = 50)
        Label(err, text = msg, font = ("Mincho", 30)).place(x = 15, y = 200)
        Button(err, text = "Back to Update Function", command = err.destroy, font = ("Mincho", 30)).place(x = 40, y = 300)

    # Success Message
    def success():
        Connection().updateMember(memid, name.get(), faculty.get(), phone.get(), email.get())
        suc = Toplevel(root)
        suc.geometry("400x400")
        suc.configure(background = "#5ae895")

        Label(suc, text = "Success!", font = ("Mincho", 50)).place(x = 100, y = 50)
        Label(suc, text = "ALS Membership Updated.", font = ("Mincho", 30)).place(x = 30, y = 150)
        Button(suc, text = "Create Another Member", command = goToCreate, font = ("Mincho", 30)).place(x = 45, y = 250)
        Button(suc, text = "Back to Update Function", command = suc.destroy, font = ("Mincho", 30)).place(x = 40, y = 300)

    def checkInput():
        if not name.get() or not faculty.get or not phone.get() or not email.get():
            error("Missing or Incomplete Fields")
        elif name.get().isnumeric() or any(x.isdigit() for x in name.get()) or any(y.isalpha() for y in phone.get()):
            error("Incorrect Fields")
        else:
            confirmUpdate()

    def confirmUpdate():
        d = Toplevel(root)
        d.geometry("500x200")

        def f():
            d.destroy()
            success()

        d_msg = Label(d, text = "Please Confirm Updated Details to Be Correct")
        d_msg.grid(row = 0, column = 0)

        Label(d, text="Membership ID", bg="#F9FBF2").grid(row=1, column=0, sticky="W")
        Label(d, text=memid, bg="#F9FBF2").grid(row=1, column=1, sticky="W")
        Label(d, text="Name", bg="#F9FBF2").grid(row=2, column=0, sticky="W")
        Label(d, text=name.get(), bg="#F9FBF2").grid(row=2, column=1, sticky="W")
        Label(d, text="Faculty", bg="#F9FBF2").grid(row=3, column=0, sticky="W")
        Label(d, text=faculty.get(), bg="#F9FBF2").grid(row=3, column=1, sticky="W")
        Label(d, text="Phone Number", bg="#F9FBF2").grid(row=4, column=0, sticky="W")
        Label(d, text=phone.get(), bg="#F9FBF2").grid(row=4, column=1, sticky="W")
        Label(d, text="Email Address", bg="#F9FBF2").grid(row=5, column=0, sticky="W")
        Label(d, text=email.get(), bg="#F9FBF2").grid(row=5, column=1, sticky="W")
        
        confirm = Button(d, text = "Confirm Update", command = f)
        confirm.grid(row = 6, column = 0)
        backButton = Button(d, text = "Back to Update Function", command = lambda: d.destroy())
        backButton.grid(row = 6, column = 1)

    # Update Member
    Button(root, text = "Update Member", command = checkInput, fg = "#8a4a22", highlightbackground = "#d4ac79", font = ("Mincho", 30)).place(x = 240, y = 450, width = 340, height = 80)
    
    # Back to Membership Menu
    Button(root, text = "Back to Membership Menu", command = backToMemMenu, fg = "#8a4a22", highlightbackground = "#d4ac79", font = ("Mincho", 25)).place(x = 240, y = 560, width = 340, height = 80)
    
    frame.mainloop()