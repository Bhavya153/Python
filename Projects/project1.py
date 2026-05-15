print("Welcome to the Interactive Personal Data Collector! \n")

name = input("Please Enter your name: ")
age = int(input("Please Enter your age: "))
height = float(input("Please Enter your Height: "))
fav = int(input("Please Enter your favourite number: "))
birthyear = 2026 - age

print("\nThank You Here is the information we collected: \n")

print("Name:", name, "(Type: ", type(name),", Memory Address: ", id(name),")" )
print("Age:", age, "(Type: ", type(age),", Memory Address: ", id(age),")" )
print("Height:", height, "(Type: ", type(height),", Memory Address: ", id(height),")" )
print("Favourite No.:", fav, "(Type: ", type(fav),", Memory Address: ", id(fav),") \n" )

print("Your birth year is approximately: ", birthyear, "(Based on your age: ", age,") \n")

print("Thank you for using Interactive Personal Data Collector! Goodbye! ")
