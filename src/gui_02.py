import tkinter as tk
from tkinter import messagebox


def show_login():

    login_success = False

    root = tk.Tk()
    root.title("Login")
    root.geometry("400x200")

    tk.Label(
        root,
        text="Username:"
    ).grid(row=0, column=0, padx=10, pady=10)

    tk.Label(
        root,
        text="Password:"
    ).grid(row=1, column=0, padx=10, pady=10)

    username_entry = tk.Entry(root)
    username_entry.grid(row=0, column=1)

    password_entry = tk.Entry(
        root,
        show="*"
    )
    password_entry.grid(row=1, column=1)

    def attempt_login():
        nonlocal login_success

        username = username_entry.get()
        password = password_entry.get()

        if username == "admin" and password == "root":
            login_success = True
            root.destroy()
        else:
            messagebox.showerror(
                "Fehler",
                "Falscher Login"
            )

    tk.Button(
        root,
        text="Login",
        command=attempt_login
    ).grid(
        row=2,
        column=0,
        columnspan=2,
        pady=10
    )

    root.mainloop()

    return login_success