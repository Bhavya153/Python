import random
import string


def generate_random_number():
    try:
        min = int(input("Enter minimum number: "))
        max = int(input("Enter maximum number: "))

        num = random.randint(min, max)

        print("Generated Random Number:", num)

    except:
        print("Please enter valid numbers")




def generate_random_list():
    try:
        size = int(input("Enter list size: "))
        min = int(input("Enter minimum value: "))
        max = int(input("Enter maximum value: "))

        list = []

        for i in range(size):
            num = random.randint(min, max)
            list.append(num)

        print("Generated Random List:")
        print(list)

    except:
        print("Please enter valid numbers")




def generate_password():
    try:
        length = int(input("Enter password length: "))

        characters = (string.ascii_letters + string.digits + string.punctuation)

        password = ""

        for i in range(length):
            password += random.choice(characters)

        print("Generated Password:", password)

    except:
        print("Please enter a valid length")




def generate_otp():
    otp = ""

    for i in range(6):
        otp += str(random.randint(0, 9))

    print("Generated OTP:", otp)




def random_sampling():
    data = ["Apple","Banana","Mango", "Orange", "Grapes", "Watermelon","Pineapple","Papaya" ]

    try:
        num = int(input("How many items should be selected? "))

        sample = random.sample(data, num)

        print("Random Sample:")
        print(sample)

    except:
        print("Invalid number or number is too large")


def random_menu():
    while True:
        print("\n==============================")
        print("Random Data Generation")
        print("==============================")

        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Random Dataset Sampling")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        match choice:

            case "1":
                generate_random_number()

            case "2":
                generate_random_list()

            case "3":
                generate_password()

            case "4":
                generate_otp()

            case "5":
                random_sampling()

            case "6":
                break

            case _:
                print("Invalid choice.")
