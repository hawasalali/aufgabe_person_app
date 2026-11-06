import tkinter as tk
from tkinter import messagebox
from manager import PersonManager


class PersonGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Person Manager")
        self.root.geometry("1000x600")

        self.manager = PersonManager()

        # Name
        tk.Label(root, text="Name:").grid(
            row=0, column=0, padx=10, pady=10
        )

        self.name_entry = tk.Entry(root, width=30)
        self.name_entry.grid(
            row=0, column=1
        )

        # Age
        tk.Label(root, text="Age:").grid(
            row=1, column=0, padx=10, pady=10
        )

        self.age_entry = tk.Entry(root, width=30)
        self.age_entry.grid(
            row=1, column=1
        )

        # Email
        tk.Label(root, text="Email:").grid(
            row=2, column=0, padx=10, pady=10
        )

        self.email_entry = tk.Entry(root, width=30)
        self.email_entry.grid(
            row=2, column=1
        )

        # File name
        tk.Label(root, text="File name:").grid(
            row=0, column=2, padx=20
        )

        self.file_entry = tk.Entry(root, width=20)
        self.file_entry.grid(
            row=0, column=3
        )

        # Load Buttons
        tk.Button(
            root,
            text="load csv",
            command=self.load_csv,
            width=12
        ).grid(row=0, column=4, padx=5)

        tk.Button(
            root,
            text="load json",
            command=self.load_json,
            width=12
        ).grid(row=1, column=4, padx=5)

        tk.Button(
            root,
            text="load xml",
            command=self.load_xml,
            width=12
        ).grid(row=2, column=4, padx=5)

        # Save Buttons
        tk.Button(
            root,
            text="save csv",
            command=lambda: self.save_file("csv"),
            width=12
        ).grid(row=0, column=5, padx=5)

        tk.Button(
            root,
            text="save json",
            command=lambda: self.save_file("json"),
            width=12
        ).grid(row=1, column=5, padx=5)

        tk.Button(
            root,
            text="save xml",
            command=lambda: self.save_file("xml"),
            width=12
        ).grid(row=2, column=5, padx=5)

        # Add
        tk.Button(
            root,
            text="Add",
            command=self.add_person,
            width=12
        ).grid(
            row=3,
            column=1,
            pady=20
        )

        # Show
        tk.Button(
            root,
            text="Show",
            command=self.show_persons,
            width=12
        ).grid(
            row=3,
            column=3,
            pady=20
        )

        # Textfeld
        self.text = tk.Text(
            root,
            width=120,
            height=20
        )

        self.text.grid(
            row=4,
            column=0,
            columnspan=6,
            padx=10,
            pady=10
        )

    def add_person(self):

        try:
            name = self.name_entry.get().strip()
            age = int(self.age_entry.get().strip())
            email = self.email_entry.get().strip()

            self.manager.add_person(
                name,
                age,
                email
            )

            messagebox.showinfo(
                "Erfolg",
                "Person hinzugefügt"
            )

            self.clear_entries()

        except Exception as e:

            messagebox.showerror(
                "Fehler",
                str(e)
            )

    def save_file(self, file_type):

        filename = self.file_entry.get().strip()

        if filename == "":
            filename = f"persons.{file_type}"

        try:

            if file_type == "csv":
                self.manager.save_csv(filename)

            elif file_type == "json":
                self.manager.save_json()

            elif file_type == "xml":
                self.manager.save_xml()

            messagebox.showinfo(
                "Erfolg",
                f"{file_type.upper()} gespeichert"
            )

        except Exception as e:

            messagebox.showerror(
                "Fehler",
                str(e)
            )

    def load_csv(self):

        self.manager.load_csv()
        self.show_persons()

        messagebox.showinfo(
            "Erfolg",
            "CSV geladen"
        )

    def load_json(self):

        self.manager.load_json()
        self.show_persons()

        messagebox.showinfo(
            "Erfolg",
            "JSON geladen"
        )

    def load_xml(self):

        self.manager.load_xml()
        self.show_persons()

        messagebox.showinfo(
            "Erfolg",
            "XML geladen"
        )

    def show_persons(self):

        self.text.delete(
            "1.0",
            tk.END
        )

        self.text.insert(
            tk.END,
            self.manager.show_persons()
        )

    def clear_entries(self):

        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)


if __name__ == "__main__":

    root = tk.Tk()

    app = PersonGUI(root)

    root.mainloop()