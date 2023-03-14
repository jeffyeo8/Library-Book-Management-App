from tkinter import *
from functools import partial
from bookBorrow import *
from bookReturn import *

def loansMenu():
    menu = Tk()
    menu.title("Loans Menu")
    menu.geometry("1500x1500")

    bg = PhotoImage(file = r"C:\Users\USER\Downloads\pain.png")
    background_label = Label(menu, image= bg)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def transition(f):
        menu.destroy()
        f()
    
    # Return back to main menu
    def backToMenu():
        menu.destroy()
        from main import start
        start()

    book_borrow = Button(menu, text = "Book  Borrow", command = partial(transition, bookBorrow), fg = "#8a4a22", highlightbackground = "#d4ac79", font = ("Mincho", 30))
    book_borrow.place(x = 395, y = 140, width = 300, height = 350)

    book_return= Button(menu, text = "Book Return", command = partial(transition, bookReturn), fg = "#8a4a22", highlightbackground = "#d4ac79", font = ("Mincho", 30))
    book_return.place(x = 745, y = 140, width = 300, height = 350)

    # Back to Main Menu
    back = Button(menu, text = "Back to Main Menu", command = backToMenu, fg = "#8a4a22", highlightbackground = "#d4ac79", font = ("Mincho", 30))
    back.place(x = 220, y = 540, width = 1000, height = 100)

    menu.mainloop()