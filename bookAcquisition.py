from tkinter import *
from connector import Connection

def bookAq():
    root = Tk()
    root.geometry("800x800")

    # Background Image
    bg = PhotoImage(file = r"C:\Users\USER\Downloads\pain.png") # Change to user's filepath for the image
    background_label = Label(root, image= bg)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    frame = LabelFrame(root, text="Book Acquisition", padx=20, pady=20, bg="#F9FBF2")
    frame.place(x = 220, y = 50)
    
    accession, title, author1, author2, author3, isbn, publisher, pubyear = (StringVar() for i in range(8))

    # Input Accession Number
    Label(frame, text="Accession Number", bg="#F9FBF2").grid(row=1, column=0, sticky="W")
    Entry(frame, textvariable = accession).grid(row=1, column=1, sticky="W")
    Label(frame, text=" ", bg="#F9FBF2").grid(row=2, column=0)

    # Input Title
    Label(frame, text="Title", bg="#F9FBF2").grid(row=3, column=0, sticky="W")
    Entry(frame, textvariable = title).grid(row=3, column=1, sticky="W")
    Label(frame, text=" ", bg="#F9FBF2").grid(row=4, column=0)

    # Input Author 1
    Label(frame, text="Author 1", bg="#F9FBF2").grid(row=5, column=0, sticky="W")
    Entry(frame, textvariable = author1).grid(row=5, column=1, sticky="W")
    Label(frame, text=" ", bg="#F9FBF2").grid(row=6, column=0)

    # Input Author 2
    Label(frame, text="Author 2", bg="#F9FBF2").grid(row=7, column=0, sticky="W")
    Entry(frame, textvariable = author2).grid(row=7, column=1, sticky="W")
    Label(frame, text=" ", bg="#F9FBF2").grid(row=8, column=0)

    # Input Author 3
    Label(frame, text="Author 3", bg="#F9FBF2").grid(row=9, column=0, sticky="W")
    Entry(frame, textvariable = author3).grid(row=9, column=1, sticky="W")
    Label(frame, text=" ", bg="#F9FBF2").grid(row=10, column=0)

    # Input ISBN
    Label(frame, text="ISBN", bg="#F9FBF2").grid(row=11, column=0, sticky="W")
    Entry(frame, textvariable = isbn).grid(row=11, column=1, sticky="W")
    Label(frame, text=" ", bg="#F9FBF2").grid(row=12, column=0)

    # Input Publisher
    Label(frame, text="Publisher", bg="#F9FBF2").grid(row=13, column=0, sticky="W")
    Entry(frame, textvariable = publisher).grid(row=13, column=1, sticky="W")
    Label(frame, text=" ", bg="#F9FBF2").grid(row=14, column=0)

    # Input Publication Year
    Label(frame, text="Publication Year", bg="#F9FBF2").grid(row=15, column=0, sticky="W")
    Entry(frame, textvariable = pubyear).grid(row=15, column=1, sticky="W")
    Label(frame, text=" ", bg="#F9FBF2").grid(row=16, column=0)

    # Go back to Books Menu
    # Go back to Books Menu
    def backToBooksMenu():
        root.destroy()
        from booksMenu import booksMenu
        booksMenu()

    def acq(acc, t, a1, a2, a3, isbn, p, py):
        if Connection().getBookDetails(isbn):
            Connection().acqDuplicate(acc, isbn)
        else:
            Connection().acqBook(acc, t, a1, a2, a3, isbn, p, py)
        success = Toplevel(root)
        success.geometry("400x400")
        success.configure(background = "#5ae895")

        Label(success, text = "Success!", font = ("Mincho", 50)).place(x = 100, y = 50)
        Label(success, text = "New Book added in Library", font = ("Mincho", 30)).place(x = 25, y = 200)
        Button(success, text = "Back to Acquisition Function", command = lambda: success.destroy(), font = ("Mincho", 30)).place(x = 15, y = 300)

    # Error Message
    def error():
        err = Toplevel(root)
        err.geometry("400x400")
        err.configure(background = "#d9414e")

        Label(err, text = "Error!", font = ("Mincho", 50)).place(x = 140, y = 50)
        Label(err, text = "Book already added;\nDuplicate, Missing\nor Incomplete fields.", font = ("Mincho", 30)).place(x = 60, y = 150)
        Button(err, text = "Back to Acquisition Function", command = lambda: err.destroy(), font = ("Mincho", 30)).place(x = 15, y = 300)

    # Check Function
    def check():
        if not accession.get() or not title.get() or not author1.get() or not isbn.get() or not publisher.get() or not pubyear.get():
            error()
        elif not pubyear.get().isnumeric():
            error()
        elif Connection().searchBook(accession.get()):
            error()
        else:
            acq(accession.get(), title.get(), author1.get(), author2.get(), author3.get(), isbn.get(), publisher.get(), pubyear.get())

    # Add New Book
    Button(root, text = "Add New Book", command = check, fg = "#8a4a22", highlightbackground = "#d4ac79", font = ("Mincho", 30)).place(x = 230, y = 550, width = 340, height = 80)

    # Back to Books Menu
    Button(root, text = "Back to Books Menu", command = backToBooksMenu, fg = "#8a4a22", highlightbackground = "#d4ac79", font = ("Mincho", 30)).place(x = 230, y = 650, width = 340, height = 80)
    frame.mainloop()
