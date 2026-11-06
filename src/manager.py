import json
import csv
import xml.etree.ElementTree as ET
from pathlib import Path
from person import Person


class PersonManager:

    def __init__(self):

        self.persons = []

        self.base_dir = Path(__file__).resolve().parent

        self.data_dir = self.base_dir / "data"

        self.data_dir.mkdir(exist_ok=True)

        self.json_file = self.data_dir / "persons.json"
        self.csv_file = self.data_dir / "persons.csv"
        self.xml_file = self.data_dir / "persons.xml"

        self.load_json()

    def add_person(self, name, age, email):

        person = Person(name, age, email)

        self.persons.append(person)

        self.save_all()

    def save_csv(self, filename="persons.csv"):

        with (self.data_dir / filename).open(
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=["name", "age", "email"]
            )

            writer.writeheader()

            for person in self.persons:

                writer.writerow(
                    {
                        "name": person.name,
                        "age": person.age,
                        "email": person.email
                    }
                )

    def save_json(self):

        with self.json_file.open(
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                [vars(person) for person in self.persons],
                file,
                indent=4,
                ensure_ascii=False
            )

    def save_xml(self):

        root = ET.Element("persons")

        for person in self.persons:

            person_element = ET.SubElement(
                root,
                "person"
            )

            ET.SubElement(
                person_element,
                "name"
            ).text = person.name

            ET.SubElement(
                person_element,
                "age"
            ).text = str(person.age)

            ET.SubElement(
                person_element,
                "email"
            ).text = person.email

        tree = ET.ElementTree(root)

        tree.write(
            self.xml_file,
            encoding="utf-8",
            xml_declaration=True
        )

    def save_all(self):

        self.save_csv()
        self.save_json()
        self.save_xml()

    def load_csv(self, filename="persons.csv"):

        file_path = self.data_dir / filename

        if not file_path.exists():
            return

        self.persons = []

        with file_path.open(
            "r",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:

                person = Person(
                    row["name"],
                    int(row["age"]),
                    row["email"]
                )

                self.persons.append(person)

    def load_json(self):

        if not self.json_file.exists():
            return

        with self.json_file.open(
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

            self.persons = [
                Person(
                    p["name"],
                    p["age"],
                    p["email"]
                )
                for p in data
            ]

    def load_xml(self):

        if not self.xml_file.exists():
            return

        tree = ET.parse(self.xml_file)

        root = tree.getroot()

        self.persons = []

        for person_element in root.findall("person"):

            person = Person(
                person_element.find("name").text,
                int(person_element.find("age").text),
                person_element.find("email").text
            )

            self.persons.append(person)

    def show_persons(self):

        return "\n".join(
            [
                f"Name: {p.name} | Age: {p.age} | Email: {p.email}"
                for p in self.persons
            ]
        )