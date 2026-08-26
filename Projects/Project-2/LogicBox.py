while True:

    print("Welcome to the Pattern Generator and Number Analyser!\n")

    print("Select an option : \n")

    print("1.Generate a pattern")
    print("2.Analyze a range of number")
    print("3.Exit")

    choice = int(input("enter your choice: "))

    match choice:

        case 1:
            rows = int(input("enter rows number: "))

            print("\npattern is:")

            for i in range(1, rows + 1):
                for j in range(1, i + 1):
                    print("*", end=" ")
                print()

        case 2:
            first = int(input("Enter your first number: "))
            second = int(input("Enter your last number: "))

            if first > second:
                print("odd even counter")
                total = 0

                for num in range(first, second + 1):
                    if num % 2 == 0:
                        print(f"number {num} is even")
                    else:
                        print(f"number {num} is odd")

                    total = total + num
                print(f"sum of all numbers from {first} to {second} is: {total}")

            else:
                print("\ninvalid numbers\n")

        case 3:
            print("\nExiting the program. Goodbye!")
            break

        case _:
            print("invalid!")