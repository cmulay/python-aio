import csv

client_fields = ['mobile', 'name', 'age', 'emailid', 'loc']
client_database = 'travel.csv'


def displaymenu():
    print("Welcome to Travel Management System\n")
    print("1. Add Client\n")
    print("2. View Client\n")
    print("3. Update Client\n")
    print("4. Delete Client\n")
    print("5. Exit\n")


def add_student():
    print("Add Client Menu")
    global client_fields
    global client_database

    client_data = []
    for field in client_fields:
        value = input("Enter " + field + ":")
        client_data.append(value)

    with open(client_database, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([client_data])

    print("Data added successfully !")
    input("Press enter to continue")
    return


def view_student():
    print("View Client Menu")
    global client_fields
    global client_database

    print("List of Clients :")

    with open(client_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for i in client_fields:
            print(i, end='\t |')
        print("\n")

        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")

    input("Press enter to continue")


def update_student():
    print("Update Client Menu")
    global client_fields
    global client_database

    mob = input("Enter client's mobile number to update:")
    index_client = None
    update_data = []

    with open(client_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if mob == row[0]:
                    client_student = counter
                    print(f"Client's Number Found at Index value {client_student}")
                    client_data = []
                    for field in client_fields:
                        value = input("Enter " + field + ":")
                        client_data.append(value)
                    update_data.append(client_data)
                else:
                    update_data.append(row)
                counter += 1

    if index_client is not None:
        with open(client_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows([update_data])

    else:
        print("No client entries found for that Number")

    input("Enter any key to continue")


def delete_student():
    print("Delete Client Menu")
    global client_fields
    global client_database

    roll_number = input("Please enter client number:")
    client_found = False
    update_data = []
    with open(client_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if roll_number != row[0]:
                    update_data.append(row)
                    counter += 1
                else:
                    client_found = True

    if client_found is True:
        with open(client_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(update_data)
        print(f"Client was deleted successfully!")

    else:
        print("Client Number not found in database")

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
        print("Thanks for using Travel Management System")
        exit()
    else:
        print("Wrong Choice!")
