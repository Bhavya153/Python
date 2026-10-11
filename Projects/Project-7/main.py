from utility_package.datetime_module import datetime_menu
from utility_package.math_module import math_menu
from utility_package.random_module import random_menu
from utility_package.uuid_module import uuid_menu
from utility_package.file_module import file_menu
from utility_package.explorer import explorer_menu

while True:

    print("\n======================================")
    print("   Welcome to Multi-Utility Toolkit   ")
    print("======================================")
  
    print("1. Date and Time Operations")
    print("2. Mathematical Operations")
    print("3. Random Data Generation")
    print("4. Generate Unique Identifiers (UUID)")
    print("5. File Operations (Custom Module)")
    print("6. Explore Module Attributes (dir())")
    print("7. Exit")

    choice = input("Enter your choice: ")

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
            print("\n======================================")
            print("Thank you for using the Multi-Utility Toolkit ")
            print("======================================")
            break

        case _:
            print("Invalid")
