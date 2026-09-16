📊 Data Analyzer and Transformer Program

A simple and interactive Python-based Data Analyzer and Transformer that allows users to enter, analyze, filter, sort, and perform calculations on a 1D array of integer data.


✨ Features
Option	Feature	Description
1️⃣	Input Data	Enter the size and values of a 1D array
2️⃣	Display Data Summary	Display total elements, minimum, maximum, sum, and average
3️⃣	Factorial	Calculate the factorial of a number using recursion
4️⃣	Filter Data	Filter values using a threshold and a lambda function
5️⃣	Sort Data	Sort data in ascending or descending order
6️⃣	Dataset Statistics	Calculate and return minimum, maximum, sum, and average
7️⃣	Exit	Exit the program
🛠️ Concepts Used

This project demonstrates several fundamental Python programming concepts:

🐍 Python Functions

🔄 for loops

🔀 match-case

📋 Lists

🧮 Mathematical calculations

🔁 Recursion

⚡ Lambda functions

🔎 filter()

📈 List sorting

↩️ Returning multiple values

⌨️ User input

🧠 Conditional statements

📂 Project Structure
Data-Analyzer-and-Transformer/
│
├── main.py
└── README.md


main.py contains the complete Python program.

🚀 How to Run
1. Clone the Repository
git clone https://github.com/your-username/your-repository-name.git

2. Navigate to the Project Directory
cd Data-Analyzer-and-Transformer

3. Run the Python Program
python main.py


Make sure Python 3.10 or later is installed because the program uses match-case.

🖥️ Program Menu

When the program starts, you will see:

Welcome to Data Analyzer and Transformer Program

1. Input Data
2. Display Data Summary (Built-in Functions)
3. Calculate Factorial (Recursion)
4. Filter Data by Threshold (Lambda Function)
5. Sort Data
6. Display Dataset Statistics (Return Multiple data)
7. exit Program

Please enter your choice:

📌 Feature Explanation
1️⃣ Input Data

Allows the user to specify the number of elements and enter integer values.

Example:

Enter Size of Array:
5

Enter Data for a 1D array:
10
25
5
40
15


The values are stored in a Python list.

2️⃣ Display Data Summary

Displays basic information about the dataset:

Data Summary:

- Total Elements: 5
- Minimum Value: 5
- Maximum Value: 40
- Sum of all values: 95
- Average value: 19.0


This feature demonstrates the use of separate functions for calculating different statistics.

3️⃣ Calculate Factorial

Calculates the factorial of a number using recursion.

For example:

Enter a number to calculate its factorial: 5

Factorial of 5 is: 120


The recursive function calculates:

5 × 4 × 3 × 2 × 1 = 120

4️⃣ Filter Data by Threshold

Uses Python's filter() function together with a lambda function.

For example, if the dataset is:

10, 25, 5, 40, 15


and the threshold is:

20


The output will be:

Filtered Data (Values >= 20):

25, 40

5️⃣ Sort Data

The program provides two sorting options:

Choose sorting option:
1. Ascending
2. Descending

Ascending
5, 10, 15, 25, 40

Descending
40, 25, 15, 10, 5


Python's built-in sort() method is used for this operation.

6️⃣ Display Dataset Statistics

This option calculates multiple statistics in a single function and returns them together.

The function returns:

Minimum Value
Maximum Value
Total / Sum
Average


Example:

Dataset Statistics:

- Minimum Value: 5
- Maximum Value: 40
- Sum of all values: 95
- Average value: 19.0


This demonstrates returning multiple values from a Python function.

🧠 Learning Objectives

The project was created to practice and demonstrate:

How to create and call functions

How to work with Python lists

How to use loops for data processing

How recursion works

How lambda functions work

How filter() can process data

How to sort lists

How to return multiple values from a function

How to build a menu-driven console application

⚠️ Important Notes

The program currently works with integer values.

Data is stored in a global list named data.

Selecting Input Data multiple times will append new values to the existing dataset.

Factorial is calculated recursively and is intended for non-negative integers.

The program requires Python 3.10+ for match-case.

🎥 Explanation Video
▶️ Project Explanation & Demonstration

Video: Watch the Project Explanation Video

🔗 

👨‍💻 Author

Bhavya Shah


⭐ Support

If you found this project useful or helpful for learning Python, consider giving the repository a ⭐ on GitHub!

📜 License

This project is created for educational and learning purposes.