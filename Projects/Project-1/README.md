Interactive Personal Data Collector — README
🧑‍💻 Interactive Personal Data Collector

A simple and beginner-friendly Python console application that collects personal information from the user and displays the entered data along with its data type and memory address.

It also calculates an approximate birth year based on the user's age.

✨ Features
👤 Collects the user's name
🎂 Collects the user's age
📏 Collects the user's height
🔢 Collects the user's favourite number
📅 Calculates the approximate birth year
🐍 Displays the Python data type of each value
💾 Displays the memory address using Python's id() function
💬 Provides a simple interactive console experience
🛠️ Technologies Used
Python 3
input() — for taking user input
int() — for converting input to integers
float() — for converting height to a decimal number
type() — for identifying data types
id() — for displaying the object's memory identity
🚀 How to Run
1. Make sure Python is installed

Check your Python version:

python --version

2. Save the program

Save the code in a file such as:

personal_data_collector.py

3. Run the program
python personal_data_collector.py

🖥️ Example
Welcome to the Interactive Personal Data Collector!

Please Enter your name: Alex
Please Enter your age: 20
Please Enter your Height: 5.8
Please Enter your favourite number: 7

Thank You Here is the information we collected:

Name: Alex (Type: <class 'str'>, Memory Address: 123456789)
Age: 20 (Type: <class 'int'>, Memory Address: 123456789)
Height: 5.8 (Type: <class 'float'>, Memory Address: 123456789)
Favourite No.: 7 (Type: <class 'int'>, Memory Address: 123456789)

Your birth year is approximately: 2006
(Based on your age: 20)

Thank you for using Interactive Personal Data Collector! Goodbye!


Note: Memory addresses shown by id() can be different each time the program runs.

🧠 Concepts Demonstrated
Variables

The program stores user information in variables such as:

name
age
height
fav
birthyear

Type Conversion

User input is initially received as a string. The program converts numeric values using:

int()
float()

Data Types

The program demonstrates three common Python data types:

Input	Python Type
Name	str
Age	int
Height	float
Favourite Number	int
type()

The type() function tells us the type of an object:

type(age)

id()

The id() function returns the identity of an object during its lifetime:

id(age)

Basic Calculation

The approximate birth year is calculated with:

birthyear = 2026 - age

⚠️ Important Note

This project is intended for Python learning and practice. The entered information is only used by the running program and is not automatically stored in a database or sent anywhere.

The birth year is only an approximation, because the calculation does not consider whether the user's birthday has already occurred in the current year.

📚 Learning Outcomes

By completing this project, beginners can practice:

Taking input from users
Working with variables
Converting data types
Using type()
Using id()
Performing arithmetic calculations
Formatting console output
Building a basic interactive Python program
🎥 Video Explanation

Video Explanation:
