from tkinter import *
from functools import partial
from bookReservation import *
from cancelReservation import *

def reserveMenu():
    menu = Tk()
    menu.title("Reservations Menu")
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

    reserve = Button(menu, text = "Book Reservation", command = partial(transition, bookReservation), fg = "#8a4a22", highlightbackground = "#d4ac79", font = ("Mincho", 30))
    reserve.place(x = 395, y = 140, width = 300, height = 350)

    cancel= Button(menu, text = "Reservation\nCancellation", command = partial(transition, cancelReservation), fg = "#8a4a22", highlightbackground = "#d4ac79", font = ("Mincho", 30))
    cancel.place(x = 745, y = 140, width = 300, height = 350)

    back = Button(menu, text = "Back to Main Menu", command = backToMenu, fg = "#8a4a22", highlightbackground = "#d4ac79", font = ("Mincho", 30))
    back.place(x = 220, y = 540, width = 1000, height = 100)

    menu.mainloop()