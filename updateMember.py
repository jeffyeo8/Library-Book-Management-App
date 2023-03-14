from tkinter import *
from actuallyUpdateMember import *
from connector import Connection

def updateMember():
    root = Tk()
    root.geometry("800x800")

    # Background Image
    bg = PhotoImage(file = r"C:\Users\USER\Downloads\pain.png")
    background_label = Label(root, image= bg)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    frame = LabelFrame(root, text="Membership Update ", padx=20, pady=20, bg="#F9FBF2")
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
        Label(suc, text = "ALS Membership Updated.", font = ("Mincho", 30)).place(x = 30, y = 200)
        Button(suc, text = "Back to Update Function", command = lambda: suc.destroy(), font = ("Mincho", 30)).place(x = 40, y = 300)
    
    # Error Message
    def error(msg):
        err = Toplevel(root)
        err.geometry("400x400")
        err.configure(background = "#d9414e")

        Label(err, text = "Error!", font = ("Mincho", 50)).place(x = 140, y = 50)
        Label(err, text = msg, font = ("Mincho", 30)).place(x = 100, y = 200)
        Button(err, text = "Back to Update Function", command = lambda: err.destroy(), font = ("Mincho", 30)).place(x = 40, y = 300)

    # Check Input
    def checkInput():
        if not memid.get():
            error("Missing Input")
        else:
            check()

    def check():
        res = Connection().searchMember(memid.get())
        if res:
            root.destroy()
            actuallyUpdateMember(memid.get())
            success()
        else:
            error("Nonexistent\nMembership ID")


    # Return back to main menu
    def backToMenu():
        root.destroy()
        from main import start
        start()

    # Update Member
    Button(root, text = "Update Member", command = checkInput, fg = "#8a4a22", highlightbackground = "#d4ac79", font = ("Mincho", 30)).place(x = 230, y = 400, width = 340, height = 80)
    
    # Back to Main Menu
    Button(root, text = "Back to Main Menu", command = backToMenu, fg = "#8a4a22", highlightbackground = "#d4ac79", font = ("Mincho", 30)).place(x = 230, y = 510, width = 340, height = 80)

    frame.mainloop()