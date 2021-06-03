from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("Authentication")
root.config(bg="#e76f51")
root.geometry("500x600")


class Authentication:
    def __init__(self, window):
        self.username = Label(window, text="Enter Username:", font="25")
        self.username.config(bg="#e76f51", fg="#2a9d8f")
        self.username.place(relx="0.4", rely="0.1")

        self.user_entry = Entry(window)
        self.user_entry.place(relx="0.37", rely="0.2")

        self.password = Label(window, text="Enter Password", font="25")
        self.password.config(bg="#e76f51", fg="#2a9d8f")
        self.password.place(relx="0.4", rely="0.4")

        self.pass_entry = Entry(window)
        self.pass_entry.place(relx="0.37", rely="0.5")

        self.authenticate = Button(window, text="Authenticate", command=self.Auth)
        self.authenticate.config(bg="#e9c46a", fg="#2a9d8f")
        self.authenticate.place(relx="0.42", rely="0.6")

        self.user_pass = {'Adam': 'bruh', 'Ronald': 'dudette', 'zoe': 'dude'}

    def Auth(self):
        name = self.user_entry.get()
        pw = self.pass_entry.get()
        try:
            if name == "" or pw == "":
                messagebox.showerror(message="Please enter details")

            elif name in self.user_pass:
                if pw == self.user_pass[name]:
                    root.destroy()
                    import window
                else:
                    messagebox.showerror(message="Password incorrect")
            else:
                messagebox.showerror(message="Username not found")
        except ValueError:
            messagebox.showerror("error")


Authentication(root)
root.mainloop()
