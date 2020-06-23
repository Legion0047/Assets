from tkinter import *
from tkinter.ttk import *

from Entity import entity as entity

class Assets(Frame):

    def budget(self):
        print("hello")

    def switch(self):
        for i in self.assets:
            if self.factions.get() == i.name:
                i.place(self, 1, 2)
            else:
                i.destroy()


    def __init__(self, window):
        super(Assets, self).__init__(window)

        self.assets = []

        self.assets.append(entity(self, "UNSC", 0, 0, 0, [entity(self, "Core Sector", 5, 1, 10, [entity(self, "Farming", 1, 0, 0)]), entity(self, "East Sector", 5, 1, 10, [entity(self, "Military", 1, 0, 0)])]))
        self.assets.append(entity(self, "Hiigarans", 0, 0, 0, [entity(self, "Cor-Hig", 1, 0, 0)]))
        self.assets.append(entity(self, "Tau", 0, 0, 0, [entity(self, "Tau", 1, 0, 0)]))


        self.factions = Combobox(self, width=15)

        for i in self.assets:
            self.factions['values'] = (*self.factions['values'], i.name)
        self.factions.grid(column=0, row=0, sticky=W)

        self.switch_btn = Button(self, text="switch faction", command=self.switch)
        self.switch_btn.grid(column=1, row=0, sticky=W)

        # Blanks

        blanks = []

        for i in range(10):
            blanks.append(Label(self, width=25, background="gray"))
            blanks[i].grid(column=i, row=1)

        # Labels


        name = Label(self, text="Name", width=20)
        name.grid(column=0, row=2)

        dev = Label(self, text="Development", width=20)
        dev.grid(column=0, row=3)

        mult = Label(self, text="Multiplier", width=20)
        mult.grid(column=0, row=4)

        raw = Label(self, text="Income", width=20)
        raw.grid(column=0, row=5)



if __name__ == "__main__":
    window = Tk()
    window.geometry('1280x720')
    window.title("Assets")


    main = Assets(window)
    main.pack(fill="both", expand=True)

    window.mainloop()