from tkinter import *
from tkinter.ttk import *


class Entry(Entry):
    def __init__(self, parent):
        self.parent = parent
        Entry.__init__(self, self.parent)

        self.__alignment = W
        self.__column = 0
        self.__padding = (0, 0)
        self.__placed = False
        self.__row = 0


    def Disable(self):
        self.configure(state=DISABLED)


    def Enable(self):
        self.configure(state=NORMAL)


    def Get_Text(self):
        return self.get()


    def Move_Cursor(self, characterCount):
        if characterCount != 0:
            self.xview_scroll(characterCount, UNITS)


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


    def Set_Text(self, text):
        self.delete(0, tk.END)
        self.insert(0, text)
        self.Move_Cursor(len(text))


    def Set_Width(self, width):
        self.configure(width=width)
