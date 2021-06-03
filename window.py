from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Exception Handling")
root.geometry("500x300")
root.config(bg="#e76f51")


class EH:
    def __init__(self, window):
        self.title = Label(window, text="Enter Amount:", font="25")
        self.title.config(bg="#e76f51", fg="#2a9d8f")
        self.title.place(relx="0.4", rely="0.3")

        self.input = Entry(window)
        self.input.place(relx="0.35", rely="0.5")

        self.button = Button(window, text="Check", command= self.check)
        self.button.config(bg="#e9c46a", fg="#2a9d8f")
        self.button.place(relx="0.45", rely="0.6")
        self.amount = 3000

    def check(self):
        try:
            if int(self.input.get()) == "":
                messagebox.showerror("Error", message="Enter appropriate amount")
            else:
                if int(self.input.get()) >= 3000:
                    messagebox.showerror("Error", message="Insufficiant funds")
                else:
                    messagebox.showinfo("Congrats", message="You Qualify!")
        except ValueError:
            messagebox.showerror("Error", message="enter amount")


EH(root)
root.mainloop()
