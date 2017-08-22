from tkinter import *
from tkinter.ttk import *


class toplevel(Toplevel):
    def __init__(self, parent):
        self.parent = parent
        Toplevel.__init__(self, self.parent)


    def Destroy(self):
        for child in self.winfo_children():
            child.destroy()
        self.destroy()


    def Expandable_Column(self, column, state=True):
        if state == True: self.columnconfigure(column, weight=1)
        else: self.columnconfigure(column, weight=0)


    def Expandable_Row(self, row, state=True):
        if state == True: self.rowconfigure(row, weight=1)
        else: self.rowconfigure(row, weight=0)
    

    def Set_Title(self, title):
        self.title(title)
