print('=' * 28)
print('Welcome to Smart Calculator')
print('=' * 28)

print('Instruction:'
      '\n➤ Enter 0 to stop the input and calculate')

store = []


def addition():
    print('Addition Menu')
    number = float(input('Enter a number: '))
    input_count = 0
    answer = 0
    while number != 0:
        answer += number
        input_count += 1
        number = float(input('Enter another number: '))
    return [answer, input_count]


def multiplication():
    print('Subtraction Menu')
    number = float(input("Enter the number: "))
    input_count = 0
    answer = 1
    while number != 0:
        answer *= number
        input_count += 1
        number = float(input('Enter another number: '))
    return [answer, input_count]


def help_avg():
    number = float(input('Enter a number: '))
    input_count = 0
    answer = 0
    while number != 0:
        answer += number
        input_count += 1
        number = float(input('Enter another number: '))
    return [answer, input_count]


def average():
    print('Average Menu')
    avg = help_avg()
    input_count = avg[1]
    add = avg[0]
    ans = add / input_count
    return [ans, input_count]


def menu():
    print('\n1. Perform Addition'
          '\n2. Perform Multiplication'
          '\n3. Perform Average'
          '\n4. Exit')


while True:
    menu()
    choice = int(input('\nEnter your choice [1 - 5]: '))
    if choice != 5:
        if choice == 1:
            store = addition()
            print(f'\nTotal Inputs: {store[1]}\nAddition: {store[0]}')
        elif choice == 2:
            store = multiplication()
            print(f'\nTotal Inputs: {store[1]}\nMultiplication: {store[0]}')
        elif choice == 3:
            store = average()
            print(f'\nTotal Inputs: {store[1]}\nAverage: {store[0]}')
        elif choice == 4:
            break
        else:
            print('Invalid Choice')
    else:
        break
