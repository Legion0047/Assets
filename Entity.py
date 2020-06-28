from functools import partial
from random import randint

from tkinter import *
from tkinter.ttk import *

class entity:
    # Name, +x to any roll in sub entities/this entity, +10*x% to budget in any sub entities/this entity, +x to the budget, sub entity
    def __init__(self, window, name="New Entity", dev=0, bonus=0, mult=0, raw=0, entities=None):
        if entities is None:
            entities = []
        self.window = window
        self.name = name
        self.dev = dev
        self.bonus = bonus
        self.mult = mult
        self.raw = raw
        self.entities = entities

        # The entries for the entities stats

        self.name_e = Entry(self.window, width=15)
        self.name_e.delete(0, END)
        self.name_e.insert(0, self.name)

        self.dev_e = Entry(self.window, width=15)
        self.dev_e.delete(0, END)
        self.dev_e.insert(0, self.dev)

        self.bonus_e = Entry(self.window, width=15)
        self.bonus_e.delete(0, END)
        self.bonus_e.insert(0, self.bonus)

        self.mult_e = Entry(self.window, width=15)
        self.mult_e.delete(0, END)
        self.mult_e.insert(0, self.mult)

        self.raw_e = Entry(self.window, width=15)
        self.raw_e.delete(0, END)
        self.raw_e.insert(0, self.raw)

        # The button to create a new entity

        self.add_btn = Button(self.window, width=15, text="Add Entity", command=self.add)

        # A button to remove entities

        self.remove_btn = []

        for i in range(len(self.entities)):
            self.remove_btn.append(Button(self.window, width=15, text="Remove Entity", command=partial(self.remove, i)))

    def load(self, data):
        for i in data:
            self.entities.append(entity(self.window, i['name'], int(i['dev']), int(i['bonus']), int(i['mult']), int(i['raw'])))
            self.remove_btn.append(Button(self.window, width=15, text="Remove Entity", command=partial(self.remove, len(self.entities)-1)))
            self.entities[-1].load(i['entities'])

    def save(self, data):
        data.append({
            'name': '%s' % self.name,
            'dev': '%i' % self.dev,
            'bonus': '%i' % self.bonus,
            'mult': '%i' % self.mult,
            'raw': '%i' % self.raw,
            'entities': []
        })
        for i in self.entities:
            i.save(data[-1]['entities'])

    def calcBudget(self, bonus=0):
        current = self.raw
        if len(self.entities) == 0:
            for i in range(self.dev+1):
                current += randint(1, 10)
            return int((current+self.bonus+int(bonus))*(1+(self.mult/10)))
        else:
            for i in self.entities:
                current += i.calcBudget(self.bonus+int(bonus))
            return int(current*(1+(self.mult/10)))

    def place(self, col, row):

        # Placing new Entries

        self.name_e = Entry(self.window, width=15)
        self.name_e.delete(0, END)
        self.name_e.insert(0, self.name)
        self.name_e.grid(column=col, row=row)

        self.dev_e = Entry(self.window, width=15)
        self.dev_e.delete(0, END)
        self.dev_e.insert(0, self.dev)
        self.dev_e.grid(column=col, row=row+1)

        self.bonus_e = Entry(self.window, width=15)
        self.bonus_e.delete(0, END)
        self.bonus_e.insert(0, self.dev)
        self.bonus_e.grid(column=col, row=row+2)

        self.mult_e = Entry(self.window, width=15)
        self.mult_e.delete(0, END)
        self.mult_e.insert(0, self.mult)
        self.mult_e.grid(column=col, row=row+3)

        self.raw_e = Entry(self.window, width=15)
        self.raw_e.delete(0, END)
        self.raw_e.insert(0, self.raw)
        self.raw_e.grid(column=col, row=row+4)

        # Placing the button to add new entities

        self.add_btn = Button(self.window, width=15, text="Add Entity", command=self.add)
        self.add_btn.grid(column=col, row=row+5)

        temp = row

        self.remove_btn = []

        # Remove entity buttons
        for i in range(len(self.entities)):
            self.remove_btn.append(Button(self.window, width=15, text="Remove Entity", command=partial(self.remove, i)))

        row+=4
        for i in range(len(self.entities)):
            col+=1
            self.remove_btn[i].grid(column=col, row=row)
            (temp, col) = self.entities[i].place(col, row+1)

        return (temp,col)

    def destroy_gui(self):
        self.name_e.destroy()
        self.dev_e.destroy()
        self.bonus_e.destroy()
        self.mult_e.destroy()
        self.raw_e.destroy()

        self.add_btn.destroy()

        for i in self.remove_btn:
            i.destroy()

        for i in self.entities:
            i.destroy_gui()

    def update(self):
        self.name = self.name_e.get()
        self.dev = int(self.dev_e.get())
        self.bonus = int(self.bonus_e.get())
        self.mult = int(self.mult_e.get())
        self.raw = int(self.raw_e.get())

        for i in self.entities:
            i.update()

    def add(self):
        self.entities.append(entity(self.window))
        self.remove_btn.append(Button(self.window, width=15, text="Remove Entity", command=partial(self.remove, len(self.entities)-1)))

    def remove(self, number):
        for i in range(len(self.remove_btn)):
            if i == number:
                self.destroy_gui()
                self.entities.pop(i)
                self.remove_btn.pop(i)

    def toString(self):
        line = "Name: %s, Dev: %i, Bonus: %i, Mult: %i, Raw: %i\n" % (self.name, self.dev, self.bonus, self.mult, self.raw)
        for i in self.entities:
            line += "    "+i.toString()
        return line
