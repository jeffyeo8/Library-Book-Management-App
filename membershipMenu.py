from tkinter import *
from functools import partial
from createMember import *
from deleteMember import *
from updateMember import *

def membershipMenu():
    menu = Tk()
    menu.title("Membership Menu")
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
        

    member_creation = Button(menu, text = "Membership\nCreation", command = partial(transition, createMember), fg = "#8a4a22", highlightbackground = "#d4ac79", font = ("Mincho", 30))
    member_creation.place(x = 220, y = 140, width = 300, height = 350)

    member_deletion= Button(menu, text = "Membership\nDeletion", command = partial(transition, deleteMember), fg = "#8a4a22", highlightbackground = "#d4ac79", font = ("Mincho", 30))
    member_deletion.place(x = 570, y = 140, width = 300, height = 350)

    member_update = Button(menu, text = "Membership\nUpdate", command = partial(transition, updateMember), fg = "#8a4a22", highlightbackground = "#d4ac79", font = ("Mincho", 30))
    member_update.place(x = 920, y = 140, width = 300, height = 350)

    back = Button(menu, text = "Back to\nMain Menu", command = backToMenu, fg = "black", bg = "lightgreen", font = ("Mincho", 30))
    back.place(x = 220, y = 540, width = 1000, height = 100)

    menu.mainloop()

