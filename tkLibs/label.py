from tkinter import *
from tkinter.ttk import *


class label(Label):
    def __init__(self, parent):
        self.parent = parent
        Label.__init__(self, self.parent)

        self.__alignment = W
        self.__column = 0
        self.__padding = (0, 0)
        self.__placed = False
        self.__row = 0
        
        self.Set_Font(('Helvetica', 9, 'bold'))


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


    def Set_Font(self, font):
        self.configure(font=font)


    def Set_Padding(self, x, y):
        self.__padding = (x, y)
        if self.__placed:
            self.grid(padx=self.__padding[0], pady=self.__padding[1])


    def Set_Text(self, text):
        self.configure(text=text)
