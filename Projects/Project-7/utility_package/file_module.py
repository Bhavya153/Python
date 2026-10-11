def create_file():
    filename = input("Enter file name: ")

    try:
        with open(filename, "w") as file:
            file.write("")

        print("File created successfully.")

    except Exception as error:
        print("Error:", error)


def write_to_file():
    filename = input("Enter file name: ")
    data = input("Enter data to write: ")

    try:
        with open(filename, "w") as file:
            file.write(data)

        print("Data written successfully.")

    except Exception as error:
        print("Error:", error)


def read_file():
    filename = input("Enter file name: ")

    try:
        with open(filename, "r") as file:
            data = file.read()

        print("\nFile Content:")
        print(data)

    except FileNotFoundError:
        print("File does not exist.")


def append_to_file():
    filename = input("Enter file name: ")
    data = input("Enter data to append: ")

    try:
        with open(filename, "a") as file:
            file.write("\n" + data)

        print("Data appended successfully.")

    except Exception as error:
        print("Error:", error)


def file_menu():
    while True:
        print("\n==============================")
        print("File Operations")
        print("==============================")

        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        match choice:

            case "1":
                create_file()

            case "2":
                write_to_file()

            case "3":
                read_file()

            case "4":
                append_to_file()

            case "5":
                break

            case _:
                print("Invalid choice.")
