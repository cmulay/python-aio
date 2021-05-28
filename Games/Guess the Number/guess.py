import random

number_limit = 30

print('==== The Guess Number Game ====\n')
print('What is this game?\n'
      'Computer will think of a number and you have to guess it !\n')
choice = input('Ready to play [Y/N]:')
print('Great !\n'
      'Computer has thought of a number. Let\'s see if you can guess it right!')
if choice == 'y' or 'Y':
    computers_choice = random.randint(1, number_limit)
    guess = 0
    while guess != computers_choice:
        guess = int(input(f'Guess the number between 1 & {number_limit}: '))
        if guess < computers_choice:
            print('You guessed wrong! too low.')
        elif guess > computers_choice:
            print('Oops! too high.')
    print(f'Damn Right! You guessed it {computers_choice}')
else:
    exit()
