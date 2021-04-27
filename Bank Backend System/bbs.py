# Student's Bank Backend System

import csv

account_fields = ['accountnumber', 'accounttype', 'pannumber', 'holder', 'age', 'emailid', 'phone', 'address',
                  'balance']
account_database = 'bank.csv'


def displaymenu():
    print("Welcome to Student's Bank Backend System\n")
    print("1. Open Account\n")
    print("2. View Account\n")
    print("3. Update Account\n")
    print("4. Delete Account\n")
    print("5. Exit\n")


def create_account():
    print("Open an Account")
    global account_fields
    global account_database

    account_data = []
    for field in account_fields:
        value = input("Enter " + field + ":")
        account_data.append(value)

    with open(account_database, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([account_data])

    print("Data added successfully !")
    input("Press enter to continue")
    return


def view_account():
    print("View all Account Holder's")
    global account_fields
    global account_database

    print("List of all Account Holders :")

    with open(account_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for i in account_fields:
            print(i, end='\t |')
        print("\n")

        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")

    input("Press enter to continue")


def update_account():
    print("Update Account Menu")
    global account_fields
    global account_database

    account_number = input("Enter your account number to update:")
    index_student = None
    update_data = []

    with open(account_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if account_number == row[0]:
                    index_holder = counter
                    print(f"Account Number Found at Index value {index_holder}")
                    account_data = []
                    for field in account_fields:
                        value = input("Enter " + field + ":")
                        account_data.append(value)
                    update_data.append(account_data)
                else:
                    update_data.append(row)
                counter += 1

    if index_student is not None:
        with open(account_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows([update_data])

    else:
        print("No entries found for that Roll Number")

    input("Enter any key to continue")


def close_account():
    print("Close Account Menu")
    global account_fields
    global account_database

    account_number = input("Please enter Account Number:")
    account_found = False
    update_data = []
    with open(account_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if account_number != row[0]:
                    update_data.append(row)
                    counter += 1
                else:
                    account_found = True

    if account_found is True:
        with open(account_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(update_data)
        print(f"Account {account_number} was deleted successfully!")

    else:
        print("Account Number not found in database")

    input("Press enter to continue")


while True:
    displaymenu()
    choice = int(input("Enter your choice:"))
    if choice == 1:
        create_account()
    elif choice == 2:
        view_account()
    elif choice == 3:
        update_account()
    elif choice == 4:
        close_account()
    elif choice >= 5:
        exit()
        print("Thanks for using Student's Bank Backend System")
        print("Developed by - Chinmay Mulay")
