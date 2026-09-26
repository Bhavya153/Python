class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Person created with name: {self.name} and age: {self.age}.")



class Employee:

    def __init__(self, name, age, employee_id, salary):
        self.name = name
        self.age = age
        self.__employee_id = employee_id
        self.__salary = salary

    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def get_salary(self):
        return self.__salary
    
    def set_salary(self, salary):
        self.__salary = salary


    def display(self):
        print("Employee Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.__employee_id)
        print("Salary:", self.__salary)



class Manager(Employee):

    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def display(self):
        print("Manager Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.get_employee_id())
        print("Salary:", self.get_salary())
        print("Department:", self.department)


def create_person():

    name = input("\nEnter Name: ")
    age = int(input("Enter Age: "))

    person = Person(name, age)
    person.display()

    return person


def create_employee():

    name = input("\nEnter Name: ")
    age = int(input("Enter Age: "))
    employee_id = input("Enter Employee ID: ")
    salary = float(input("Enter Salary: "))

    employee = Employee(name, age, employee_id, salary)

    employee.display()

    return employee


def create_manager():

    name = input("\nEnter Name: ")
    age = int(input("Enter Age: "))
    employee_id = input("Enter Employee ID: ")
    salary = float(input("Enter Salary: "))
    department = input("Enter Department: ")

    manager = Manager(name, age, employee_id, salary, department)
    manager.display()

    return manager



def show_details(objects):

    print("---------------")
    if not objects:
        print("No records available.")
    else:
        for obj in objects:
            obj.display()
    print("---------------")




objects = []

print("\n--- Python OOP Project; Employe Management System---")

while True:

    print("\nChoose an operation:")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Show Details")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    match choice:

        case "1":
            person = create_person()
            objects.append(person)

        case "2":
            employee = create_employee()
            objects.append(employee)

        case "3":
            manager = create_manager()
            objects.append(manager)

        case "4":
            show_details(objects)

        case "5":
            print("\nThank you for using Employee Management System.")
            break

        case _:
            print("\nInvalid")