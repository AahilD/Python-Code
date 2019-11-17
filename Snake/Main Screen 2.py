from tkinter import * #Tk, Label, Button

class TitleScreen:
    def __init__(self, master):
        self.master = master
        master.title("Welcome")

        self.label = Label(master, text="Snake")
        self.label.pack()

        self.greet_button = Button(master, text="Start", command=self.start)
        self.greet_button.pack()

        self.close_button = Button(master, text="Exit", command=master.quit)
        self.close_button.pack()

    def start(self):
        print("YAM")

root = Tk()
my_gui = TitleScreen(root)
root.mainloop()