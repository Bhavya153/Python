🛠️ Multi-Utility Toolkit

A Python-based modular utility application that combines Date & Time, Mathematics, Random Data, UUID, File Handling, and Module Exploration into one easy-to-use toolkit.

📌 Project Overview

The Multi-Utility Toolkit is a menu-driven Python application designed to demonstrate the practical use of:

📅 Date and Time operations

🧮 Mathematical calculations

🎲 Random data generation

🔐 UUID generation

📁 File handling

🔍 Python module exploration using dir()

📦 Custom Python packages and modules

🔀 match-case menu selection

⚠️ Exception handling

The project is divided into multiple modules to keep the code organized, reusable, and easy to maintain.

✨ Features
📅 1. Date and Time Operations

The Date and Time module provides:

Display current date and time

Calculate difference between two dates

Format dates into a custom format

Stopwatch

Countdown timer

🧮 2. Mathematical Operations

The Mathematics module provides:

Factorial calculation

Compound interest calculation

Trigonometric calculations

Area calculation for:

Circle

Rectangle

Triangle

🎲 3. Random Data Generation

The Random module provides:

Generate a random number

Generate a random list

Generate a random password

Generate a 6-digit OTP

Select random items from a dataset

🆔 4. UUID Generation

The UUID module generates a unique identifier using Python's built-in uuid module.

Example:

Generated UUID: 7f8c2e7b-3c4a-4c6d-9f2e-123456789abc

📁 5. File Operations

The File module provides:

Create a new file

Write data to a file

Read file contents

Append data to a file

🔍 6. Module Explorer

The Explorer module allows the user to enter a Python module name and view its available attributes using:

dir()


For example:

Enter module name to explore: math


The program displays the available attributes of the math module.

📂 Project Structure
Multi-Utility-Toolkit/
│
├── main.py
│
└── utility_package/
    │
    ├── __init__.py
    ├── datetime_module.py
    ├── math_module.py
    ├── random_module.py
    ├── uuid_module.py
    ├── file_module.py
    └── explorer.py

📄 Files Description
File	Purpose
main.py	Main application and primary menu
__init__.py	Defines utility_package as a Python package
datetime_module.py	Date, time, stopwatch, and countdown operations
math_module.py	Mathematical calculations
random_module.py	Random number, list, password, OTP, and sampling operations
uuid_module.py	UUID generation
file_module.py	File creation, writing, reading, and appending
explorer.py	Explores module attributes using dir()
🔄 How the Program Works

The program starts from main.py.

The main menu provides seven options:

======================================
      Welcome to Multi-Utility Toolkit
======================================

1. Date and Time Operations
2. Mathematical Operations
3. Random Data Generation
4. Generate Unique Identifiers (UUID)
5. File Operations (Custom Module)
6. Explore Module Attributes (dir())
7. Exit


The user selects an option, and the corresponding module menu is called.

For example:

match choice:
    case "1":
        datetime_menu()

    case "2":
        math_menu()

    case "3":
        random_menu()

    case "4":
        uuid_menu()

    case "5":
        file_menu()

    case "6":
        explorer_menu()

    case "7":
        break


This makes the main program simple and easy to understand.

🧩 Modular Programming

One of the main concepts demonstrated in this project is modular programming.

Instead of putting every operation into one large Python file, the project separates functionality into different modules.

For example:

from utility_package.math_module import math_menu


This allows main.py to use the mathematical operations without containing all the mathematical code itself.

Benefits of modular programming

✅ Cleaner code

✅ Easier maintenance

✅ Code reusability

✅ Better organization

✅ Easier debugging

✅ Separate responsibilities for each module

🔀 Match-Case

The project uses Python's match-case statement for menu selection.

Example:

match choice:
    case "1":
        datetime_menu()

    case "2":
        math_menu()

    case "3":
        random_menu()

    case _:
        print("Invalid choice.")


The _ case works as the default case when the user enters an invalid option.

Note: match-case requires Python 3.10 or later.

⚠️ Exception Handling

The project uses try-except blocks to handle invalid user input and file-related errors.

Example:

try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Please enter a valid integer.")


This prevents the program from crashing when the user enters invalid data.

The project handles situations such as:

Invalid numbers

Invalid dates

Invalid file names

Missing files

Invalid module names

Invalid menu choices

🐍 Python Modules Used

The project uses several built-in Python modules.

datetime

Used for:

import datetime


Date and time operations.

time

Used for:

import time


Stopwatch and countdown functionality.

math

Used for:

import math


Mathematical and trigonometric calculations.

random

Used for:

import random


Random numbers, passwords, OTPs, and random sampling.

string

Used for:

import string


Letters, digits, and punctuation for password generation.

uuid

Used for:

import uuid


Generating unique identifiers.

📁 File Handling

The project demonstrates Python file handling using:

open()


Different file modes are used:

Mode	Purpose
"w"	Write/create a file
"r"	Read a file
"a"	Append data to a file

Example:

with open(filename, "w") as file:
    file.write(data)


The with statement automatically handles closing the file.

🔍 Module Exploration

The Explorer module demonstrates the use of:

dir()


The user can enter a module name such as:

math


The program imports the module dynamically:

module = __import__(module_name)


Then it displays the available attributes:

attributes = dir(module)
print(attributes)


This is useful for exploring Python modules and understanding their available functions and attributes.

▶️ How to Run
1. Install Python

Make sure Python 3.10 or newer is installed.

Check your Python version:

python --version


or:

python3 --version

2. Open the Project Folder

Open a terminal inside the project directory.

Example:

cd Multi-Utility-Toolkit

3. Run the Main Program

Run:

python main.py


The main menu will appear:

======================================
      Welcome to Multi-Utility Toolkit
======================================

1. Date and Time Operations
2. Mathematical Operations
3. Random Data Generation
4. Generate Unique Identifiers (UUID)
5. File Operations (Custom Module)
6. Explore Module Attributes (dir())
7. Exit

💡 Example Usage
Generate a UUID

Select:

4


Output:

==============================
Generate Unique Identifiers
==============================

Generated UUID: 4e7c3b2a-...

Generate a Random Password

Select:

3


Then select the password option:

Enter password length: 12


Example output:

Generated Password: A7@kP2!xQ9#m

Calculate Date Difference

Select:

1


Then:

Enter first date (YYYY-MM-DD): 2026-01-01
Enter second date (YYYY-MM-DD): 2026-01-15

Difference: 14 days

🎯 Concepts Demonstrated

This project demonstrates several important Python concepts:

📦 Packages

📄 Modules

🔗 Import statements

🔀 match-case

🔁 while loops

🔢 User input

🧮 Mathematical operations

📅 Date and time handling

🎲 Random data generation

🆔 UUID generation

📁 File handling

🔍 dir()

🛡️ Exception handling

🧩 Functions

🔄 Modular programming

🌟 Why This Project?

The Multi-Utility Toolkit is designed as a practical Python project that brings multiple concepts together in one application.

Instead of creating separate small programs for each operation, the project combines them into one structured toolkit using custom modules and a Python package.

This makes it a useful demonstration of basic-to-intermediate Python programming concepts.

🎥 Video Explanation
link: 

👨‍💻 Author
Bhavya Shah

Project: Multi-Utility Toolkit
Language: Python 🐍

⭐ Thank you for checking out the Multi-Utility Toolkit!