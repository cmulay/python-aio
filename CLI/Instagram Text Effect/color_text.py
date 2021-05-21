# Note: Colorama has limited color options
import colorama
from colorama import Back, Fore

colorama.init(autoreset=True)

text = input("Enter your text: ")
print('Style 1:')
print(Fore.BLACK + text)
print(Fore.RED + text)
print(Fore.GREEN + text)
print(Fore.YELLOW + text)
print(Fore.BLUE + text)
print(Fore.MAGENTA + text)
print(Fore.CYAN + text)
print('\nStyle 2:')
print(Fore.BLACK + Back.WHITE + text)
print(Fore.RED + Back.CYAN + text)
print(Fore.GREEN + Back.MAGENTA + text)
print(Fore.YELLOW + Back.BLUE + text)
print(Fore.BLUE + Back.YELLOW + text)
print(Fore.MAGENTA + Back.GREEN + text)
print(Fore.CYAN + Back.RED + text)
print(Fore.WHITE + Back.BLACK + text)
