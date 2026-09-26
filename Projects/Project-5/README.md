👨‍💼 Employee Management System

A simple Python OOP-based Employee Management System built to demonstrate core Object-Oriented Programming concepts such as classes, objects, inheritance, encapsulation, constructors, method overriding, getters/setters, and polymorphism.

This project provides a simple menu-driven console interface where users can create and manage different types of people, employees, and managers.

📌 Features

👤 Create a Person

👨‍💼 Create an Employee

👨‍💼 Create a Manager

📋 Display details of all created records

🔐 Encapsulation of Employee ID and Salary

🧬 Demonstrates inheritance using Employee and Manager

🔄 Demonstrates method overriding with display()

🎯 Demonstrates polymorphism

🖥️ Simple interactive command-line interface

🧠 OOP Concepts Used
Concept	Implementation
Class & Object	Person, Employee, and Manager classes
Constructor	__init__() methods
Encapsulation	Private __employee_id and __salary
Inheritance	Manager inherits from Employee
Method Overriding	display() is overridden
Getters & Setters	Employee ID and Salary methods
Polymorphism	obj.display() works with different object types
super()	Used to initialize inherited attributes
🏗️ Class Structure
Person
   │
   └── Employee
          │
          └── Manager

Person

Stores basic information:

Name

Age

Employee

Extends Person and adds:

Employee ID

Salary

Employee ID and Salary are encapsulated using private attributes.

Manager

Extends Employee and adds:

Department

🖥️ Menu

When the program starts, users are presented with the following menu:

--- Python OOP Project; Employee Management System ---

Choose an operation:
1. Create a Person
2. Create an Employee
3. Create a Manager
4. Show Details
5. Exit

📋 Example
Creating an Employee
Enter Name: Bhavya
Enter Age: 21
Enter Employee ID: EMP101
Enter Salary: 50000

Employee Details:
Name: Bhavya
Age: 21
Employee ID: EMP101
Salary: 50000.0

Creating a Manager
Enter Name: Rahul
Enter Age: 35
Enter Employee ID: MGR101
Enter Salary: 85000
Enter Department: IT

Manager Details:
Name: Rahul
Age: 35
Employee ID: MGR101
Salary: 85000.0
Department: IT

⚙️ Requirements

🐍 Python 3.10+

No external libraries are required.

The project uses Python's match-case statement, which requires Python 3.10 or newer.

🚀 How to Run
1. Clone the repository
git clone YOUR_REPOSITORY_LINK

2. Navigate to the project directory
cd employee-management-system

3. Run the program
python main.py

🎥 Video Explanation

▶️ Watch the Video Explanation

link: 

👨‍💻 Author

Bhavya Shah

Made with ❤️ using Python & Object-Oriented Programming