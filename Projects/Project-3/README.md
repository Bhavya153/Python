🎓 Student Data Organizer

A simple and interactive Python console-based Student Data Organizer that allows you to add, view, update, delete, and manage student information efficiently.

📌 About The Project

The Student Data Organizer is a beginner-friendly Python project designed to manage student records using a Python dictionary.

The program provides a menu-driven interface where users can:

➕ Add new students
👀 View all student records
✏️ Update existing student information
🗑️ Delete student records
📚 Display all subjects offered
🚪 Exit the application

This project is useful for understanding fundamental Python concepts such as dictionaries, loops, conditional statements, sets, user input, and pattern matching (match-case).

✨ Features
Feature	Description
➕ Add Student	Add a student with ID, name, age, grade, DOB, and subjects
👀 View Students	Display all stored student information
✏️ Update Student	Modify an existing student's details
🗑️ Delete Student	Remove a student using their Student ID
📚 Subjects Offered	Display a unique list of all subjects
🚪 Exit	Safely exit the application
🛠️ Technologies Used
🐍 Python 3.10+
📦 Python Dictionary
🔄 while Loop
🔀 match-case
🔢 Sets
⌨️ User Input
🧠 Conditional Statements
📂 Data Structure

Student information is stored inside a Python dictionary:

students = {
    101: {
        "name": "John",
        "age": 18,
        "grade": "12th",
        "dob": "2008-05-10",
        "subjects": ["Math", "Physics", "Computer"]
    }
}


The Student ID is used as the dictionary key, while the student's information is stored as another dictionary.

🚀 How to Run
1️⃣ Clone the Repository
git clone https://github.com/your-username/student-data-organizer.git

2️⃣ Navigate to the Project Folder
cd student-data-organizer

3️⃣ Run the Python Program
python student_data_organizer.py

🖥️ Program Menu

When you run the program, you will see:

Welcome to the Student Data Organizer!

Select an option:
1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Display Subjects Offered
6. Exit

Enter your choice:

📖 Explanation
1. ➕ Add Student

The Add Student option collects:

Student ID
Name
Age
Grade
Date of Birth
Subjects

The information is then stored in the students dictionary.

2. 👀 View Students

The program checks whether any student records exist.

If records are available, it loops through the dictionary and displays the stored information.

If there are no records, it displays:

No students found!

3. ✏️ Update Student

The user enters a Student ID.

If the ID exists, the program allows the user to enter updated information.

If the ID doesn't exist:

Student not found!

4. 🗑️ Delete Student

The user provides the Student ID that should be deleted.

The Python del statement removes the student from the dictionary:

del students[delete_id]

5. 📚 Display Subjects Offered

The program uses a set to collect subjects from all students.

allSubjects = set()


A set automatically prevents duplicate subjects, so each subject is displayed only once.

6. 🚪 Exit

Selecting option 6 terminates the while loop using:

break


The program then displays:

Exiting the program. Goodbye!

🎥 Explanation Video

🔗 Watch Explanation Video : 

📸 Sample Output
Welcome to the Student Data Organizer!

Select an option:
1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Display Subjects Offered
6. Exit

Enter your choice : 1

Student ID: 101
Name: Rahul
Age: 18
Grade: 12
Date of Birth (YYYY-MM-DD): 2008-03-15
Subjects (comma-separated): Math,Physics,Computer

Student added successfully!

🧠 Python Concepts Demonstrated
📌 Variables
📌 Dictionaries
📌 Nested Dictionaries
📌 Lists
📌 Sets
📌 while Loops
📌 for Loops
📌 if-else Conditions
📌 match-case
📌 User Input
📌 Type Conversion
📌 Dictionary Methods
📌 break Statement

👨‍💻 Author

Bhavya Shah

⭐ If you found this project useful, consider giving the repository a star!