from tkinter import *
from tkinter102 import MyGui

mainwin = Tk()
mainwin.geometry("500x300+300+300")
Label(mainwin, text=__name__).pack()

popup = Toplevel()
popup.geometry("150x150+100+100")
Label(popup, text='Attach').pack(side=LEFT)
MyGui(popup).pack(side=RIGHT)
mainwin.mainloop()
