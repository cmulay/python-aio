def d2b_converter(number):
    if number >= 1:
        d2b_converter(number // 2)
    print(number % 2, end='')


if __name__ == '__main__':
    print('This program converts decimal number to binary')
    dec_val = int(input('Number to convert:'))
    if dec_val != 0:
        d2b_converter(dec_val)

    else:
        print('Invalid Input')
