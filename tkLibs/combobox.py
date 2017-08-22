from tkinter import *
from tkinter.ttk import *


class combobox(Combobox):
    def __init__(self, parent):
        self.parent = parent
        Combobox.__init__(self, self.parent)
        
        self.__alignment = W
        self.__column = 0
        self.__padding = (0, 0)
        self.__placed = False
        self.__row = 0


    def Disable(self):
        self.configure(state=DISABLED)


    def Enable(self):
        self.configure(state=NORMAL)


    def Place(self, row, column):
        self.__row = row
        self.__column = column
        self.__placed = True
        
        self.grid(row=self.__row, column=self.__column, padx=self.__padding[0], pady=self.__padding[1], sticky=self.__alignment)


    def Set_Alignment(self, alignment):
        alignmentOptions = {'left': W, 'right': E, 'top': N, 'bottom': S}

        alignment = alignment.lower()
        if alignment in alignmentOptions.keys():
            self.__alignment = alignmentOptions[alignment]
            if self.__placed:
                self.grid(sticky=self.__alignment)


    def Set_Padding(self, x, y):
        self.__padding = (x, y)
        if self.__placed:
            self.grid(padx=self.__padding[0], pady=self.__padding[1])


    def Set_Values(self, *values):
        self.configure(values=values)


    def Set_Width(self, width):
        self.configure(width=width)
