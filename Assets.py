from tkinter import *
from tkinter.ttk import *

from Entity import entity as entity

class Assets(Frame):

    def budget(self):
        for i in self.assets:
            if self.factions.get() == i.name:
                self.budget_lbl.configure(text=i.calcBudget())

    def switch(self):
        for i in self.assets:
            if self.factions.get() == i.name:
                i.place(self, 1, 2)
            else:
                i.destroy()

    def update(self):
        for i in self.assets:
            if self.factions.get() == i.name:
                i.update()

    def __init__(self, window):
        super(Assets, self).__init__(window)

        self.assets = []

        self.assets.append(entity(self, "UNSC", 0, 0, 0, 0, [entity(self, "Core Sector", 0,5, 1, 10, [entity(self, "Farming", 1, 1, 0, 0), entity(self, "Military", 1, 1, 0, 0)]), entity(self, "South Sector", 0, 5, 1, 10, [entity(self, "Farming", 1, 1, 0, 0), entity(self, "Military", 1, 1, 0, 0)]), entity(self, "East Sector", 0, 5, 1, 10, [entity(self, "Farming", 1, 1, 0, 0), entity(self, "Military", 1, 1, 0, 0)])]))
        self.assets.append(entity(self, "Hiigarans", 0, 0, 0, 0, [entity(self, "Cor-Hig", 6, 1, 0, 0)]))
        self.assets.append(entity(self, "Tau", 0, 0, 0, 0, [entity(self, "Tau", 4, 2, 4, 3)]))

        # Faction Switch

        self.factions = Combobox(self, width=15)

        for i in self.assets:
            self.factions['values'] = (*self.factions['values'], i.name)
        self.factions.grid(column=0, row=0, sticky=W)

        self.switch_btn = Button(self, width=15, text="switch faction", command=self.switch)
        self.switch_btn.grid(column=1, row=0, sticky=W)

        # Calculate Budget

        self.budget_lbl = Label(self, width=15, text="0")
        self.budget_lbl.grid(column=2, row=0, sticky=W)

        self.budget_btn = Button(self, width=15, text="Calculate Budget", command=self.budget)
        self.budget_btn.grid(column=3, row=0, sticky=W)

        # Update stats

        self.update_btn = Button(self, width=15, text="Update Stats", command=self.update)
        self.update_btn.grid(column=4, row=0, sticky=W)

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



if __name__ == "__main__":
    window = Tk()
    window.geometry('1280x720')
    window.title("Assets")


    main = Assets(window)
    main.pack(fill="both", expand=True)

    window.mainloop()
