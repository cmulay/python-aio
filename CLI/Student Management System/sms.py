# Developed by Chinmay Mulay on Date: 19-04-2021
# Student Management System
# Add, Delete, Update, Display
# Student - Name, Roll Number, Age, Email ID, Phone Number.

import csv

student_fields = ['roll', 'name', 'age', 'emailid', 'phone']
student_database = 'student.csv'


def displaymenu():
    print("Welcome to Mini Student Management System\n")
    print("1. Add Student\n")
    print("2. View Student\n")
    print("3. Update Student\n")
    print("4. Delete Student\n")
    print("5. Exit\n")


def add_student():
    print("Add Student Menu")
    global student_fields
    global student_database

    student_data = []
    for field in student_fields:
        value = input("Enter " + field + ":")
        student_data.append(value)

    with open(student_database, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([student_data])

    print("Data added successfully !")
    input("Press enter to continue")
    return


def view_student():
    print("View Student Menu")
    global student_fields
    global student_database

    print("List of Students :")

    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for i in student_fields:
            print(i, end='\t |')
        print("\n")

        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")

    input("Press enter to continue")


def update_student():
    print("Update Student Menu")
    global student_fields
    global student_database

    roll_number = input("Enter student's roll number to update:")
    index_student = None
    update_data = []

    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if roll_number == row[0]:
                    index_student = counter
                    print(f"Student Roll Number Found at Index value {index_student}")
                    student_data = []
                    for field in student_fields:
                        value = input("Enter " + field + ":")
                        student_data.append(value)
                    update_data.append(student_data)
                else:
                    update_data.append(row)
                counter += 1

    if index_student is not None:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows([update_data])

    else:
        print("No entries found for that Roll Number")

    input("Enter any key to continue")


def delete_student():
    print("Delete Student Menu")
    global student_fields
    global student_database

    roll_number = input("Please enter roll number:")
    student_found = False
    update_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if roll_number != row[0]:
                    update_data.append(row)
                    counter += 1
                else:
                    student_found = True

    if student_found is True:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(update_data)
        print(f"Roll Number {roll_number} was deleted successfully!")

    else:
        print("Roll Number not found in database")

    input("Press enter to continue")


while True:
    displaymenu()
    choice = int(input("Enter your choice:"))
    if choice == 1:
        add_student()
    elif choice == 2:
        view_student()
    elif choice == 3:
        update_student()
    elif choice == 4:
        delete_student()
    elif choice >= 5:
        exit()
        print("Thanks for using Mini Student Management System")
        print("Developed by - Chinmay Mulay")
    else:
        print("Wrong Choice!")
