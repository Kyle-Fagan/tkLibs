from tkinter import *
from tkinter.ttk import *


class listbox(Listbox):
    def __init__(self, parent):
        from .autoScrollbar import autoScrollbar

        self.parent = parent
        self.frame = Frame(self.parent)

        Listbox.__init__(self, self.frame)

        self.frame.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=1)

        self.horizontalScrollbar = autoScrollbar(self.frame, orient=HORIZONTAL)
        self.verticalScrollbar = autoScrollbar(self.frame)
        self.configure(xscrollcommand=self.horizontalScrollbar.Set)
        self.configure(yscrollcommand=self.verticalScrollbar.Set)
        self.horizontalScrollbar.configure(command=self.xview)
        self.verticalScrollbar.configure(command=self.yview)

        self.__column = 0
        self.__columnSpan = 1
        self.__data = []
        self.__height = 1
        self.__padding = (0, 0)
        self.__placed = False
        self.__row = 0
        self.__rowSpan = 1
        self.__width = 25


    def Clear(self):
        self.__data = []
        self.delete(0, END)


    def Get_Selection(self):
        return [self.__data[x] for x in self.curselection()]


    def Insert_Item(self, item):
        self.__data.append(item)
        self.insert(END, item)


    def Place(self, row, column):
        self.horizontalScrollbar.grid(row=1, column=0, sticky=E+W)
        self.verticalScrollbar.grid(row=0, column=1, sticky=N+S)
        self.grid(row=0, column=0, sticky=N+E+W+S)

        self.__row = row
        self.__column = column
        self.__placed = True

        self.frame.grid(row=self.__row,
                        column=self.__column,
                        columnspan=self.__columnSpan,
                        padx=self.__padding[0],
                        pady=self.__padding[1],
                        rowspan=self.__rowSpan,
                        sticky=N+E+W+S)


    def Remove_Item(self, item):
        itemIndex = self.__data.index(item)
        del self.__data[itemIndex]
        self.delete(itemIndex)


    def Set_Command(self, event, handle):
        self.bind(event, handle)


    def Span_Columns(self, columnCount):
        self.__columnSpan = columnCount
        if self.__placed:
            self.frame.grid(columnspan=self.__columnSpan)


    def Span_Rows(self, rowCount):
        self.__rowSpan = rowCount
        if self.__placed:
            self.frame.grid(rowspan=self.__rowSpan)


    def Set_Height(self, height):
        self.__height = height
        self.frame.configure(height=self.__height)


    def Set_Padding(self, x, y):
        self.__padding = (x, y)
        if self.__placed:
            self.frame.grid(padx=self.__padding[0], pady=self.__padding[1])


    def Set_Width(self, width):
        self.__width = width
        self.frame.configure(width=self.__width)