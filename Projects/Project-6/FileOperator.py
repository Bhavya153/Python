import os
from datetime import datetime


class Journal:

    def __init__(self):
        self.filename = "journal.txt"


    def add_entry(self):
        entry = input("Enter your journal entry: ")

        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            file = open(self.filename, "a")
            file.write("[" + date + "]\n")
            file.write(entry + "\n")
            file.write("--------------------\n")
            file.close()

            print("Entry added successfully ")

        except:
            print("Error= Could not add the entry.")


    def view_entries(self):
        try:
            file = open(self.filename, "r")
            data = file.read()
            file.close()

            print("\nYour Journal Entries:")
            print(data)

        except FileNotFoundError:
            print("No journal entries found.  Start by adding a new entry! ")


    def search_entry(self):

        try:
            file = open(self.filename, "r")
            data = file.read()
            file.close()

            word = input("Enter a keyword or date to search: ")

            if word.lower() in data.lower():
                print("\nMatching Entry:")
                print(data)
            else:
                print("No entries were found for:", word)

        except FileNotFoundError:
            print("Error: The journal file does not exist.")



    def delete_entry(self):

        if os.path.exists(self.filename):
             answer = input("Are you sure you want to delete all entries? (yes/no): ")

             if answer.lower() == "yes":
                 os.remove(self.filename)
                 print("All entries deleted successfully ")
             else:
                 print("Delete cancelled. ")

        else:
         print("No entries found. ")




journal = Journal()

while True:

    print("\nWelcome to Personal Journal Manager!")

    print("1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")

    choice = input("Enter your choice: ")

    match choice:

        case "1":
            journal.add_entry()

        case "2":
            journal.view_entries()

        case "3":
            journal.search_entry()

        case "4":
            journal.delete_entry()

        case "5":
            print("Thank you for using Personal Journal Manager. Goodbye!")
            break

        case _:
            print("Invalid")
