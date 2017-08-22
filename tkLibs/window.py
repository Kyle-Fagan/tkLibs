from tkinter import *
from tkinter.ttk import *


class window(Tk):
    def __init__(self):
        Tk.__init__(self)


    def Set_Title(self, title):
        self.title(title)


    def Show(self):
        self.mainloop()
