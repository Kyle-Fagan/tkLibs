from tkinter import *
from tkinter.ttk import *


class autoScrollbar(Scrollbar):
    def Set(self, low, high):
        if float(low) <= 0.0 and float(high) >= 1.0:
            self.grid_remove()
        else:
            self.grid()
        Scrollbar.set(self, low, high)
