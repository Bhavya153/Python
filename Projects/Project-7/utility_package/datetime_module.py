import datetime
import time


def display_current_datetime():
    current = datetime.datetime.now()
    print("Current Date and Time:", current.strftime("%Y-%m-%d %H:%M:%S"))


def calculate_date_difference():
    try:
        date1 = input("Enter first date (YYYY-MM-DD): ")
        date2 = input("Enter second date (YYYY-MM-DD): ")

        date1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
        date2 = datetime.datetime.strptime(date2, "%Y-%m-%d")

        difference = abs((date2 - date1).days)

        print("Difference:", difference, "days")

    except:
        print("Invalid date format")


def format_date():
    try:
        date = input("Enter date (YYYY-MM-DD): ")
        date = datetime.datetime.strptime(date, "%Y-%m-%d")

        print("Formatted Date:", date.strftime("%d-%m-%Y"))

    except:
        print("Invalid date format")


def stopwatch():
    print("\nStopwatch started.")
    print("Press Enter to stop.")

    start = time.time()
    input()
    end = time.time()

    print("Elapsed Time:", round(end - start, 2), "seconds")


def countdown_timer():
    try:
        sec = int(input("Enter countdown time in seconds: "))

        if sec <= 0:
            print("Enter a positive number")
            return

        while sec > 0:
            print("Time remaining:", sec, "seconds")
            time.sleep(1)
            sec -= 1

        print("Time's up")

    except:
        print("Please enter a valid number")


def datetime_menu():
    while True:
        print("\n==============================")
        print("Date and Time Operations")
        print("==============================")
        print("1. Current Date and Time")
        print("2. Date Difference")
        print("3. Format Date")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                display_current_datetime()

            case "2":
                calculate_date_difference()

            case "3":
                format_date()

            case "4":
                stopwatch()

            case "5":
                countdown_timer()

            case "6":
                break

            case _:
                print("Invalid")
