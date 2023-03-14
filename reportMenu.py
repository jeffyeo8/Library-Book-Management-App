from tkinter import *
from functools import partial
from bookSearch import *
from booksOnLoan import *
from booksOnReservation import *
from outstandingFines import *
from onLoanMember import *

def reportMenu():
    menu = Tk()
    menu.title("Reports Menu")
    menu.geometry("1500x1500")

    bg = PhotoImage(file = r"C:\Users\USER\Downloads\pain.png")
    background_label = Label(menu, image= bg)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def transition(f):
        menu.destroy()
        f()

    search = Button(menu, text = "Book Search", command = partial(transition, bookSearch), fg = "#8a4a22", highlightbackground = "#d4ac79", font = ("Mincho", 30))
    search.place(x = 220, y = 80, width = 300, height = 300)

    on_loan = Button(menu, text = "Books On Loan", command = partial(transition, bookOnLoan), fg = "#8a4a22", highlightbackground = "#d4ac79", font = ("Mincho", 30))
    on_loan.place(x = 570, y = 80, width = 300, height = 300)

    on_reserve = Button(menu, text = "Books on\nReservation", command = partial(transition, bookOnReservation), fg = "#8a4a22", highlightbackground = "#d4ac79", font = ("Mincho", 30))
    on_reserve.place(x = 920, y = 80, width = 300, height = 300)

    outstanding_fines = Button(menu, text = "Oustanding Fines", command = partial(transition, outstandingFines), fg = "#8a4a22", highlightbackground = "#d4ac79", font = ("Mincho", 30))
    outstanding_fines.place(x = 220, y = 400, width = 300, height = 300)

    on_loan_member = Button(menu, text = "Books on\nLoan to Member", command = partial(transition, onLoanMember), fg = "#8a4a22", highlightbackground = "#d4ac79", font = ("Mincho", 30))
    on_loan_member.place(x = 570, y = 400, width = 300, height = 300)

    # Return back to main menu
    def backToMenu():
        menu.destroy()
        from main import start
        start()

    # Back to Main Menu
    back = Button(menu, text = "Back to Main Menu", command = backToMenu, fg = "#8a4a22", highlightbackground = "#d4ac79", font = ("Mincho", 30))
    back.place(x = 220, y = 760, width = 1000, height = 100)

    menu.mainloop()