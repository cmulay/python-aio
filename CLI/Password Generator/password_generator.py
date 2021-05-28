import random
import array

length = 12

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
alpha_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
               'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
               'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z']
alpha_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
               'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
               'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
               'Z']

key_symbols = ['~', '!', '@', '#', '$', '%', '^',
               '&', '*', '(', ')', '_', '+', '{', '}',
               ':', '|', '<', '>', '?', '-', '=', '[', ']',
               ';', '.', '/', ',']


def generate_pass():
    aio = numbers + alpha_upper + alpha_lower + key_symbols

    random_num = random.choice(numbers)
    random_upper_case = random.choice(alpha_upper)
    random_lower_case = random.choice(alpha_lower)
    random_key_symbol = random.choice(key_symbols)

    _pass = random_num + random_upper_case + random_lower_case + random_key_symbol

    for i in range(length - 4):
        _pass += random.choice(aio)
        converted_pass = array.array('u', _pass)
        random.shuffle(converted_pass)

    legit_pass = ''
    for i in converted_pass:
        legit_pass += i

    print(f'Your generated password is {legit_pass}')


while True:
    choice = str(input('Generate Password [y/n]:'))
    if choice == 'y':
        generate_pass()
    else:
        exit()
