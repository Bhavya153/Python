# 📔 Personal Journal Manager

A simple and beginner-friendly Python application for managing personal journal entries.

## ✨ About the Project

Personal Journal Manager allows users to:

- Add a new journal entry
- View all journal entries
- Search for an entry
- Delete all journal entries
- Exit the program

All journal entries are stored in a file called `journal.txt`.

## 🚀 Features

### 1. Add a New Entry ✍️

The user can enter a journal entry.

The program automatically adds the current date and time to the entry.

Example:

    [2026-10-03 16:30:45]
    Today I learned Python.
    --------------------

### 2. View All Entries 📖

The program displays all journal entries saved in `journal.txt`.

If there are no entries, the program tells the user to add a new entry.

### 3. Search for an Entry 🔎

The user can search for an entry using a keyword or date.

The search is not case-sensitive.

For example, searching for `python` can also find `Python` or `PYTHON`.

### 4. Delete All Entries 🗑️

The user can delete all journal entries.

Before deleting, the program asks for confirmation:

    Are you sure you want to delete all entries? (yes/no):

The entries are deleted only when the user enters `yes`.

### 5. Exit 🚪

The user can select option 5 to exit the program.

## 🖥️ Main Menu

When the program starts, it displays:

    Welcome to Personal Journal Manager!

    1. Add a New Entry
    2. View All Entries
    3. Search for an Entry
    4. Delete All Entries
    5. Exit

    Enter your choice:

## 📂 Project Structure

    Personal-Journal-Manager/
    │
    ├── journal.py
    ├── journal.txt
    └── README.md

The `journal.txt` file is created automatically when the first journal entry is added.

## 🛠️ Technologies Used

- Python
- File Handling
- datetime
- os
- Classes and Objects
- Functions
- match-case

## 📚 Python Concepts Used

### Class

The project uses a `Journal` class to organize the journal functions.

    class Journal:

### Constructor

The constructor sets the name of the journal file.

    def __init__(self):
        self.filename = "journal.txt"

### Functions

The project contains four main functions:

- `add_entry()`
- `view_entries()`
- `search_entry()`
- `delete_entry()`

### File Handling

The program uses append mode to add new entries:

    open(self.filename, "a")

The `a` mode adds new information to the end of the file.

The program uses read mode to view journal entries:

    open(self.filename, "r")

The `r` mode reads information from the file.

### Date and Time

The program uses `datetime` to get the current date and time.

    datetime.now()

### OS Module

The `os` module is used to check if the journal file exists and to delete it.

    os.path.exists(self.filename)

    os.remove(self.filename)

### Match-Case

The main menu uses `match-case` to select the required operation.

    match choice:

## ▶️ How to Run

### Step 1

Make sure Python 3.10 or newer is installed.

### Step 2

Create a Python file called:

    journal.py

### Step 3

Paste the Personal Journal Manager code into the file.

### Step 4

Open the terminal in the project folder.

Run:

    python journal.py

### Step 5

Choose an option from 1 to 5 and follow the instructions.

## 🎥 Video Explanation

### Topic: Personal Journal Manager – Python File Handling and OOP

The video explanation covers:

1. Introduction to the Personal Journal Manager
2. Explanation of the `Journal` class
3. Adding journal entries
4. Viewing journal entries
5. Searching for entries
6. Deleting journal entries
7. File handling using `r` and `a`
8. Using `datetime`
9. Using the `os` module
10. Using `match-case`
11. Running and demonstrating the program

### 🎬 Video Link

link: 

## 👨‍💻 Author

### Bhavya Shah

Made with 🐍 Python and ❤️
