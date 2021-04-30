import random

print('ROCK PAPER SCISSORS')
print('-' * 20)
print('\nInstructions:'
      '\n1. This game available in only Computer v/s Player mode'
      '\n2. You play 1 round at a time'
      '\n3. Use only rock, paper and scissor as input')

input('\nPress Enter to continue')
while True:
    choice = str(input('Do you want to start the game now ? [y/n]'))
    if choice == 'y':
        moves = ['rock', 'paper', 'scissor']
        computer = random.randint(0, 2)
        while True:
            user_move = str(input('Enter your choice:'))
            if user_move not in moves:
                print("That's not a valid choice. Check your spelling!")
            # TIE Only
            if user_move == 'rock' and computer == 0:
                print('\nIt\'s a TIE !')
                print('\nBoth you and computer chose Rock as your move')
                break
            elif user_move == 'paper' and computer == 1:
                print('\nIt\'s a TIE !')
                print('\nBoth you and computer chose Paper as your move')
                break
            elif user_move == 'scissor' and computer == 2:
                print('\nIt\'s a TIE !')
                print('\nBoth you and computer chose Scissor as your move')
                break
            # User Wins Only
            elif user_move == 'rock' and computer == 2:
                print('\nYou WON!')
                print('\nComputer chose Scissors as their move')
                break
            elif user_move == 'paper' and computer == 0:
                print('\nYou WON!')
                print('\nComputer chose Rock as their move')
                break
            elif user_move == 'scissor' and computer == 1:
                print('\nYou WON!')
                print('\nComputer chose Paper as their move')
                break
            # Computer Wins Only
            elif user_move == 'rock' and computer == 1:
                print('\nComputer WON!')
                print('\nComputer chose Paper as their move')
                break
            elif user_move == 'paper' and computer == 2:
                print('\nComputer WON!')
                print('\nComputer chose Paper as their move')
                break
            elif user_move == 'scissor' and computer == 0:
                print('\nComputer WON!')
                print('\nComputer chose Paper as their move')
                break
    else:
        print('Thanks for Playing !')
        break
