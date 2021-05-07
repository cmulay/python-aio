import getpass
import datetime
import csv

customer_fields = ['email', 'name']
customer_database = 'customer.csv'

sliced_fields = ['username', 'domain']
sliced_database = 'final_customer.csv'

flag = 0
temp = []

print("--------------------------------------")
print("Welcome to Advance Email Slicer System")
print("---------------------------------------")

user_name = input('Username:')
pass_word = getpass.getpass('Password:')

if user_name == 'admin' and pass_word == 'admin@123':
    current_session = datetime.datetime.now()
    log = current_session.strftime('%c')
    print('Session Logged In at ' + log + '\n')
    flag = 1

else:
    print('Invalid Credentials')
    exit()


def email_slicer():
    email = input("Enter Your Email: ").strip()
    username = email[:email.index('@')]
    domain = email[email.index('@') + 1:]
    print(f"Your username is {username} & domain is {domain}")


def menu():
    print('1. Add Information')
    print('2. View Information')
    print('3. View Username and Domains')
    print('4. Exit')


def add_info():
    print('Add Customer Information')
    global customer_fields
    global customer_database

    customer_data = []
    for field in customer_fields:
        value = input("Enter " + field + ":")
        customer_data.append(value)

    with open(customer_database, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([customer_data])

    print("Data added successfully !")

    input('Press Enter to Continue')

    return


def view_info():
    print('View Customer Information')
    global customer_fields
    global customer_database

    with open(customer_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for i in customer_fields:
            print(i, end='\t |')
        print("\n")

        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")

    input("Press enter to continue")


def perform_operation():
    global sliced_fields
    global sliced_database
    global customer_fields
    global customer_database

    with open(customer_database, "r", encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            for item in row:
                temp.append(item)

    all_emails = temp[::2]

    for i in all_emails:
        i.strip()
        stripped_username = i[:i.index('@')]
        stripped_domain = i[i.index('@') + 1:]

        sliced_data = []
        username = stripped_username
        domain = stripped_domain
        sliced_data.append(username)
        sliced_data.append(domain)

        with open(sliced_database, 'a', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows([sliced_data])

    print('View Username and Domain')
    with open(sliced_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for i in sliced_fields:
            print(i, end='\t |')
        print("\n")

        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")

    input("Press enter to continue")


if flag == 1:
    while True:
        menu()
        choice = int(input('Enter your choice:'))
        if choice == 1:
            add_info()
        elif choice == 2:
            view_info()
        elif choice == 3:
            perform_operation()
        elif choice == 4:
            current_session = datetime.datetime.now()
            log = current_session.strftime('%c')
            print('Session Ended at ' + log + '\n')
            print('Developer by - Chinmay Mulay')
            flag = 0
            break
        else:
            print('Invalid Choice. Try Again\n')
