
students = {}

while True:
    print("\nWelcome to the Student Data Organizer!\n")
    
    print("Select an option:")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")
    
    choice = int(input("Enter your choice : "))
    
    match choice:
        case 1:
            studentid = int(input("Student ID: "))
            name = input("Name: ")
            age = int(input("Age: "))
            grade = input("Grade: ")
            dob = input("Date of Birth (YYYY-MM-DD): ")
            subjects = input("Subjects (comma-separated): ").split(",")
            
            students[studentid] = {
                "name": name,
                "age": age,
                "grade": grade,
                "dob": dob,
                "subjects": subjects
            }
            print("\nStudent added successfully!\n")
            
        case 2:
            if not students:
                print("\nNo students found!\n")
            else:
                for sid, info in students.items():
                 print(f"Student ID: {sid}")
                for key, value in info.items():
                    print(f"  {key}: {value}")
                print()
                
        case 3:
            student_id = int(input("Enter Student ID to update: "))

            if student_id in students:
                students[student_id]["name"] = input("Enter Updated Name: ")
                students[student_id]["age"] = int(input("Enter Updated Age: "))
                students[student_id]["grade"] = input("Enter Updated Grade: ")
                students[student_id]["dob"] = input("Enter Updated Date of Birth (YYYY-MM-DD): ")
                students[student_id]["subjects"] = input("Enter Updated Subjects (comma-separated): ").split(",")

                print("\nStudent updated successfully!\n")
            else:
                print("\nStudent not found!\n")


        case 4:
            delete_id = int(input("Enter Student ID to delete: "))
            if delete_id in students:
                del students[delete_id]
                print("\nStudent deleted successfully!\n")
            else:
                print("\nStudent not found!\n")

        case 5:
            print("\nSubjects Offered:")
            allSubjects = set()

            for info in students.values():
              allSubjects.update(info["subjects"])

            if not allSubjects:
              print("No subjects found!")
            else:
             for subject in allSubjects:
              print(f" - {subject}")

                
        case 6:
            print("\nExiting the program. Goodbye!\n")
            break
        
        case _:
            print("Invalid\n")
