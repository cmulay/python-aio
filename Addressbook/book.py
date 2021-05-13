import csv

contact_fields = ['phone', 'label_phone', 'first_name', 'surname', 'company', 'email', 'label_email']
contact_database = 'address_book.csv'


def menu():
    print("Welcome to Address Book\n")
    print("1. Add Contact\n")
    print("2. View Contacts\n")
    print("3. Delete Contact\n")
    print("4. Exit\n")


def add_contact():
    print("Add Contact Menu")
    global contact_fields
    global contact_database

    contact_data = []
    for field in contact_fields:
        value = input("Enter " + field + ":")
        contact_data.append(value)

    with open(contact_database, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([contact_data])

    print("Data added successfully !")
    input("Press enter to continue")
    return


def view_contact():
    print("View Contact Menu")
    global contact_fields
    global contact_database

    print("List of Contacts :")

    with open(contact_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for i in contact_fields:
            print(i, end='\t |')
        print("\n")

        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")

    input("Press enter to continue")


def delete_contact():
    print("Delete Contact Menu")
    global contact_fields
    global contact_database

    phone_number = input("Please enter number:")
    contact_found = False
    update_data = []
    with open(contact_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if phone_number != row[0]:
                    update_data.append(row)
                    counter += 1
                else:
                    contact_found = True

    if contact_found is True:
        with open(contact_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(update_data)
        print(f"Contact with {phone_number} was deleted successfully!")

    else:
        print("Number not found in database")

    input("Press enter to continue")


while True:
    menu()
    choice = int(input("Enter your choice:"))
    if choice == 1:
        add_contact()
    elif choice == 2:
        view_contact()
    elif choice == 3:
        delete_contact()
    elif choice >= 4:
        exit()
        print("Thank you for using Address Book")
    else:
        print("Wrong Choice!")
