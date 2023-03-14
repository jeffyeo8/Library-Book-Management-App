from tkinter import *
from functools import partial
from bookAcquisition import *
from bookWithdrawal import *

def booksMenu():
    menu = Tk()
    menu.title("Books Menu")
    menu.geometry("1500x1500")

    bg = PhotoImage(file = r"C:\Users\USER\Downloads\pain.png")
    background_label = Label(menu, image= bg)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def transition(f):
        menu.destroy()
        f()

    def backToMenu():
        menu.destroy()
        from main import start
        start()

    book_aq = Button(menu, text = "Book Acquisition", command = partial(transition, bookAq), fg = "#8a4a22", highlightbackground = "#d4ac79", font = ("Mincho", 30))
    book_aq.place(x = 395, y = 140, width = 300, height = 350)

    book_w= Button(menu, text = "Book Withdrawal", command = partial(transition, bookW), fg = "#8a4a22", highlightbackground = "#d4ac79", font = ("Mincho", 30))
    book_w.place(x = 745, y = 140, width = 300, height = 350)

    back = Button(menu, text = "Back to Main Menu", command = backToMenu, fg = "#8a4a22", highlightbackground = "#d4ac79", font = ("Mincho", 30))
    back.place(x = 220, y = 540, width = 1000, height = 100)

    menu.mainloop()