import random

author = "Chinmay Mulay"


def dice_1():
    dice_value = random.randint(1, 6)
    input('Press any key to throw')
    print('Hold tight! It\'s rollin\'')
    if dice_value == 6:
        print(f'Damn! You got {dice_value}')
    else:
        print(f'Ayy! You got {dice_value}')


def dice_2():
    dice_one_value = random.randint(1, 6)
    dice_two_value = random.randint(1, 6)
    input('Press any key to throw dices')
    print('Hold tight! It\'s rollin\'')
    print(f'Ayy! You got one {dice_one_value} and {dice_two_value}')


def play_again():
    keep_rolling = input('\nThrow it again [y/n] ?')

    if keep_rolling == '':
        print('Didn\'t get that! Try again:')
        keep_rolling = play_again()
    return keep_rolling


print('CLI based Dice Roll')
print('\nInstructions:'
      '\n1.This game allows you to use up-to 2 virtual dices depending upon your requirement'
      '\n2.To continue rolling dice feed y'
      '\n3.To quit simply feed n')

input('\nPress any key to continue')

print('\nPlay with '
      '\n1. Single Dice '
      '\n2. Dual Dice\n')
number_of_dices = int(input('Ans [1/2]:'))
if number_of_dices == 1:
    flag = 0
    dice_1()
    keep_rolling = play_again()
elif number_of_dices == 2:
    flag = 1
    dice_2()
    keep_rolling = play_again()
else:
    print('Invalid Selection')

while keep_rolling:
    if keep_rolling == 'n':
        print(f'Developed by - {author}')
        break
    elif keep_rolling == 'y':
        if flag == 0:
            dice_1()
            keep_rolling = play_again()
        elif flag == 1:
            dice_2()
            keep_rolling = play_again()
        else:
            print('Something went wrong')
            keep_rolling = play_again()
    else:
        print('Wrong Input !!! Enter again y/n')
        keep_rolling = play_again()
