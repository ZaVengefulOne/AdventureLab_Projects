# import tkinter as tk
import tkinter
from tkinter import *
import tkinter.ttk as ttk

#
# class Window(Frame):
#     def __int__(self, master=None, bg="darkgray"):
#         Frame.__init__(self, master)
#         self.master = master
#         self.master.configure(background="darkgray")


window = Tk()
window.configure(bg="black")
frame_beast = Frame()
frame_beast.configure(bg="black", borderwidth=1)
frame_favor = Frame()
frame_favor.configure(bg="black")


# app = Window(window)

def display():
    zombieID = entry.get()
    if zombieID == "Обычный":
        Label(master=frame_beast, text="Обычный зомби = Скорость: 1, Живучесть: 1", fg="lime",
              bg="black").pack()


favorCounter = 0


def favor_callback():
    global favorCounter
    if favorCounter == 0:
        Label(master=frame_favor,
              text=f"Представитель добирается до базы детей, рассказывает ваще кто он и откуда, \n  "
                   "и встречается с выжившим военным. Между ними вероятно происходит социалка  \n"
                   "а-ля -Вы послали нас на верную смерть -Ничего не знаю, стандартный протокол, \n "
                   "вы должны были быть к этому готовы. Посоциалить с военным узнать что \n"
                   "произошло в деталях. Представитель просит найти и выделить ему терминал для \n "
                   "связи с корпорацией, чтобы он мог отправить отчёт о том что нашёл группу \n"
                   "выживших а из отряда остался только один оперативник.",
              fg="Lime",
              anchor=tkinter.CENTER,
              borderwidth=1,
              relief=tkinter.SOLID,
              justify=tkinter.CENTER,
              bg="black")\
            .pack()
        favorCounter += 1
    elif favorCounter == 1:
        Label(master=frame_favor,
              text="Coming soon",
              fg="Lime",
              borderwidth=1,
              relief=tkinter.SOLID,
              bg="black")\
            .pack()
        favorCounter += 1
    else:
        Label(master=frame_favor,
              text="Новых заданий пока нет. Конец связи.",
              fg="Lime",
              borderwidth=1,
              relief=tkinter.SOLID,
              bg="black")\
            .pack()
        favorCounter += 1


Label(master=frame_beast, text="Добро пожаловать в Зомбистиарий!", foreground="lime", background="black",
      height=5,
      font=("Arial", 25)).pack()
Label(master=frame_beast, text="Введите название зомби", fg="lime", bg="black").pack()
Button(master=frame_beast, text="Enter", command=display, fg="lime", bg="black", relief=tkinter.SOLID).pack()
Button(master=frame_favor, text="Связаться с FAVOR", command=favor_callback, fg="lime",
       background="black", relief=tkinter.SOLID).pack()
entry = Entry(master=frame_beast, fg="black", bg="lime",relief=tkinter.RAISED)
entry.pack()
frame_beast.pack()
frame_favor.pack()
window.mainloop()
