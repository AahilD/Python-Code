import tkinter as tk
#
# main application
#
class MainApp(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title("Welcome")
        self.parent.geometry("480x320")
        self.parent.resizable(width=False, height=False)
        self.parent.config(bg="gray")

        mainframe = tk.Frame(self, bg="grey", width=480, height=280 )
        mainframe.grid(column=0, row=0, sticky="WENS")
        tk.Label(mainframe, text="co-cooo").grid(column=0, row=0, sticky="WENS")

        fkeyframe = tk.Frame(self, bg="black", width=480, height=40)
        fkeyframe.grid(column=0, row=1, sticky="WENS")
        tk.Label(fkeyframe, text="fo-fooo").grid(column=0, row=0, sticky="WENS")

        self.rowconfigure(0, weight=1, minsize=280)
        self.rowconfigure(1, weight=1, minsize=40)
#
# define root element and start application
#
def main():
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()

#
# start if called from command line
#
if __name__ == '__main__':
    main()

#      0,0   MainApp (yellow)          480,0
#       +---------------------------------+
#       |   mainframe (grey, h=280)       |
#       |+-------------------------------+|
#       ||                               ||
#       ||                               ||
#       ||                               ||
#       |+-------------------------------+|
#       |   fkeyframe  (black, h=40)      |
#       |+-------------------------------+|
#       ||+----+----+----+----+----+----+||
#       ||| Bt | Bt | Bt | Bt | Bt | Bt |||
#       ||+----+----+----+----+----+----+||
#       |+-------------------------------+|
#       +---------------------------------+
#    320,0                             320,480