import csv

todo_fields = ['sr_no', 'task', 'deadline']
todo_database = 'todo.csv'


def displaymenu():
    print("PyTasker\n")
    print("1. Add Tasks\n")
    print("2. View Tasks\n")
    print("3. Mark Task Done\n")
    print("4. Exit\n")


def add_task():
    print("Add Task Menu")
    global todo_fields
    global todo_database

    do_data = []
    for field in todo_fields:
        value = input("Enter " + field + ":")
        do_data.append(value)

    with open(todo_database, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([do_data])

    print("Task added successfully !")
    input("Press enter to continue")
    return


def view_task():
    print("View Task Menu")
    global todo_fields
    global todo_database

    print("Your task list :")

    with open(todo_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for i in todo_fields:
            print(i, end='\t |')
        print("\n")

        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")

    input("Press enter to continue")


def mark_done():
    print("Mark Done Menu")
    global todo_fields
    global todo_database

    sr_number = input("Please enter serial number:")
    task_found = False
    do_data = []
    with open(todo_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if sr_number != row[0]:
                    do_data.append(row)
                    counter += 1
                else:
                    task_found = True

    if task_found is True:
        with open(todo_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(do_data)
        print(f"Task marked done successfully!")

    else:
        print("Task not found in database")

    input("Press enter to continue")


while True:
    displaymenu()
    choice = int(input("Enter your choice:"))
    if choice == 1:
        add_task()
    elif choice == 2:
        view_task()
    elif choice == 3:
        mark_done()
    elif choice == 4:
        print("Thanks for using PyTasker")
        exit()
    else:
        print("Wrong Choice!")
