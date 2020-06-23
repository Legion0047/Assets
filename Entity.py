from random import random

from tkinter import *
from tkinter.ttk import *

class entity:
    # Name, +x to any roll in sub entities/this entity, +10*x% to budget in any sub entities/this entity, +x to the budget, sub entity
    def __init__(self, window, name, dev, mult, raw, entities=None):
        self.name = name
        self.dev = dev
        self.mult = mult
        self.raw = raw
        self.entities = entities


        self.name_e = Entry(window, width=20)

        self.dev_e = Entry(window, width=20)

        self.mult_e = Entry(window, width=20)

        self.raw_e = Entry(window, width=20)

    def calcBudget(self, dev):
        current = self.raw
        if self.entities is None:
            for i in range(dev):
                current += random.randint(1, 10)
            return (current+self.dev+dev)*self.mult
        else:
            for i in self.entities:
                current += i.calcBudget(self.dev+dev)
            return current*self.mult

    def place(self, window, col, row):
        self.name_e = Entry(window, width=20)
        self.name_e.delete(0, END)
        self.name_e.insert(0, self.name)
        self.name_e.grid(column=col, row=row)

        self.dev_e = Entry(window, width=20)
        self.dev_e.delete(0, END)
        self.dev_e.insert(0, self.dev)
        self.dev_e.grid(column=col, row=row+1)

        self.mult_e = Entry(window, width=20)
        self.mult_e.delete(0, END)
        self.mult_e.insert(0, self.mult)
        self.mult_e.grid(column=col, row=row+2)

        self.raw_e = Entry(window, width=20)
        self.raw_e.delete(0, END)
        self.raw_e.insert(0, self.raw)
        self.raw_e.grid(column=col, row=row+3)

        temp = row

        if self.entities is not None:
            row+=4
            for i in self.entities:
                col+=1
                (temp, col) = i.place(window, col, row+4)

        return (temp,col)

    def destroy(self):
        self.name_e.destroy()
        self.dev_e.destroy()
        self.mult_e.destroy()
        self.raw_e.destroy()
        if self.entities is not None:
            for i in self.entities:
                i.destroy()