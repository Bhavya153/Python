import math


def calculate_factorial():
    try:
        num = int(input("Enter a number: "))

        if num < 0:
            print("Factorial is not possible for negative numbers")
        else:
            result = math.factorial(num)
            print("Factorial:", result)

    except:
        print("Please enter a valid integer")


def compound_interest():
    try:
        principal = float(input("Enter principal amount: "))
        rate = float(input("Enter rate of interest (in %): "))
        time = float(input("Enter time (in years): "))

        amount = principal * (1 + rate / 100) ** time
        interest = amount - principal

        print("Compound Interest: ", round(interest, 2))
        print("Total Amount: ", round(amount, 2))

    except:
        print("Please enter valid numbers")


def trigonometric_calculations():
    try:
        angle = float(input("Enter angle in degrees: "))
        radians = math.radians(angle)

        print("sin(", angle, ") =", round(math.sin(radians), 4))
        print("cos(", angle, ") =", round(math.cos(radians), 4))
        print("tan(", angle, ") =", round(math.tan(radians), 4))

    except:
        print("Please enter a valid number")


def area_of_shapes():
    print("\nArea of Shapes")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")

    choice = input("Enter your choice: ")

    match choice:

        case "1":
            radius = float(input("Enter radius: "))
            area = math.pi * radius * radius
            print("Area of Circle:", round(area, 2))

        case "2":
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))
            area = length * width
            print("Area of Rectangle:", round(area, 2))

        case "3":
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            area = 0.5 * base * height
            print("Area of Triangle:", round(area, 2))

        case _:
            print("Invalid")


def math_menu():
    while True:
        print("\n==============================")
        print("Mathematical Operations")
        print("==============================")

        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        match choice:

            case "1":
                calculate_factorial()

            case "2":
                compound_interest()

            case "3":
                trigonometric_calculations()

            case "4":
                area_of_shapes()

            case "5":
                break

            case _:
                print("Invalid")
