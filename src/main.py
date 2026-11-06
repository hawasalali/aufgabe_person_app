from gui_02 import show_login
from gui_01 import PersonGUI
import tkinter as tk


def main():

    if show_login():

        root = tk.Tk()

        app = PersonGUI(root)

        root.mainloop()


if __name__ == "__main__":
    main()