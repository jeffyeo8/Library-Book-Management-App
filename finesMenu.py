from tkinter import *
from functools import partial
from finePayment import *

def finesMenu():
    menu = Tk()
    menu.title("Fines Menu")
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

    payment = Button(menu, text = "Fine Payment", command = partial(transition, finePayment), fg = "#8a4a22", highlightbackground = "#d4ac79", font = ("Mincho", 30))
    payment.place(x = 570, y = 140, width = 300, height = 350)

    # Back to Main Menu
    back = Button(menu, text = "Back to Main Menu", command = backToMenu, fg = "#8a4a22", highlightbackground = "#d4ac79", font = ("Mincho", 30))
    back.place(x = 220, y = 540, width = 1000, height = 100)

    menu.mainloop()