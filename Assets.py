import json
from tkinter import *
from tkinter.ttk import *

from Entity import entity as entity

class Assets(Frame):

    def save(self):
        data = []
        for i in self.assets:
            i.save(data)
        js = {}
        js['Assets'] = data
        with open('data.txt', 'w') as outfile:
            json.dump(js, outfile, indent=4)


    def load(self):
        with open('data.txt') as json_file:
            data = json.load(json_file)
            assets = data['Assets']
            for i in assets:
                self.add(i['name'], int(i['dev']), int(i['bonus']), int(i['mult']), int(i['raw']))
                self.assets[-1].load(i['entities'])

            for i in self.assets:
                print(i.toString())

    def remove(self):
        for i in range(len(self.assets)):
            if self.factions.get() == self.assets[i].name:
                self.assets.pop(i)
                break

        self.factions['values'] = ''

        for i in self.assets:
            self.factions['values'] = (*self.factions['values'], i.name)

        if len(self.factions['values']) != 0:
            self.factions.current(len(self.factions['values'])-1)
            self.switch()


    def add(self, name="New Entity", dev=0, bonus=0, mult=0, raw=0, entities=None):
        self.assets.append(entity(self, name, dev, bonus, mult, raw, entities))

        self.factions['values'] = (*self.factions['values'], self.assets[-1].name)

        if len(self.factions['values']) != 0:
            self.factions.current(len(self.factions['values'])-1)
            self.switch()

    def clock(self):
        self.update()
        self.after(1000, self.clock)  # run itself again after 1000 ms

    def budget(self):
        for i in self.assets:
            if self.factions.get() == i.name:
                self.budget_lbl.configure(text=i.calcBudget())

    # Switches Factions, destroys old entries, places new entries
    def switch(self):
        for i in self.assets:
            i.destroy_gui()
            if self.factions.get() == i.name:
                i.place(1, 2)

    # Updates the stats of an factions entities
    def update(self):
        for i in self.assets:
            if self.factions.get() == i.name:
                i.update()

    def __init__(self, window):
        super(Assets, self).__init__(window)

        self.assets = []

        # Faction Switch

        self.factions = Combobox(self, width=15)

        for i in self.assets:
            self.factions['values'] = (*self.factions['values'], i.name)
        self.factions.grid(column=0, row=0, sticky=W)

        if len(self.factions['values']) != 0:
            self.factions.current(0)
            self.switch()

        self.switch_btn = Button(self, width=15, text="switch faction", command=self.switch)
        self.switch_btn.grid(column=1, row=0, sticky=W)

        # Calculate Budget

        self.budget_lbl = Label(self, width=15, text="0")
        self.budget_lbl.grid(column=2, row=0, sticky=W)

        self.budget_btn = Button(self, width=15, text="Calculate Budget", command=self.budget)
        self.budget_btn.grid(column=3, row=0, sticky=W)

        # Add Faction

        self.add_btn = Button(self, width=15, text="Add Faction", command=self.add)
        self.add_btn.grid(column=4, row=0, sticky=W)

        # Remove Faction

        self.remove_btn = Button(self, width=15, text="Remove Faction", command=self.remove)
        self.remove_btn.grid(column=5, row=0, sticky=W)

        # Save

        self.save_btn = Button(self, width=15, text="Save", command=self.save)
        self.save_btn.grid(column=5, row=0, sticky=W)

        # Blanks

        for i in range(20):
            blank = Label(self, width=20, background="gray")
            blank.grid(column=i, row=1)

        # Labels

        name = Label(self, text="Name", width=15)
        name.grid(column=0, row=2)

        dev = Label(self, text="Development", width=15)
        dev.grid(column=0, row=3)

        dev = Label(self, text="Bonus", width=15)
        dev.grid(column=0, row=4)

        mult = Label(self, text="Multiplier", width=15)
        mult.grid(column=0, row=5)

        raw = Label(self, text="Income", width=15)
        raw.grid(column=0, row=6)

        self.load()

        # Start the Clock
        self.clock()

if __name__ == "__main__":
    window = Tk()
    window.geometry('1280x720')
    window.title("Assets")


    main = Assets(window)
    main.pack(fill="both", expand=True)

    window.mainloop()
