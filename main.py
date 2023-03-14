from tkinter import *
from functools import partial
from membershipMenu import *
from booksMenu import *
from loansMenu import *
from reserveMenu import *
from finesMenu import *
from reportMenu import *



def start():
    menu = Tk()
    menu.title("Main Menu")
    menu.geometry("1500x1500")

    def transition(f):
        menu.destroy()
        f()

    bg = PhotoImage(file = r"C:\Users\USER\Downloads\pain.png") # Use file path of image on own computer
    background_label = Label(menu, image= bg)
    background_label.place(x=0, y=0, relheight=1, relwidth=1)

    membership = Button(menu, text = "Membership", command = partial(transition, membershipMenu), fg = "#8a4a22", highlightbackground = "#d4ac79", font = ("Mincho", 30))
    membership.place(x = 220, y = 80, width = 300, height = 300)

    books = Button(menu, text = "Books", command = partial(transition, booksMenu), fg = "#8a4a22", highlightbackground = "#d4ac79", font = ("Mincho", 30))
    books.place(x = 570, y = 80, width = 300, height = 300)
    loans = Button(menu, text = "Loans", command = partial(transition, loansMenu), fg = "#8a4a22", highlightbackground = "#d4ac79", font = ("Mincho", 30))
    loans.place(x = 920, y = 80, width = 300, height = 300)

    reserve = Button(menu, text = "Reservations", command = partial(transition, reserveMenu), fg = "#8a4a22", highlightbackground = "#d4ac79", font = ("Mincho", 30))
    reserve.place(x = 220, y = 400, width = 300, height = 300)

    fines = Button(menu, text = "Fines", command = partial(transition, finesMenu), fg = "#8a4a22", highlightbackground = "#d4ac79", font = ("Mincho", 30))
    fines.place(x = 570, y = 400, width = 300, height = 300)

    reports = Button(menu, text = "Reports", command = partial(transition, reportMenu), fg = "#8a4a22", highlightbackground = "#d4ac79", font = ("Mincho", 30))
    reports.place(x = 920, y = 400, width = 300, height = 300)

    menu.mainloop()

start()



