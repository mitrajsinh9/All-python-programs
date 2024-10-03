import colorama
from colorama import Fore, Back, Style
# Initialize colorama
colorama.init()
# Print text in different colors
print(Fore.RED + "This is red text")
print(Fore.GREEN + "This is green text")
print(Fore.BLUE + "This is blue text")
# Reset to default color
print(Style.RESET_ALL + "This is default text color")
# You can also change the background color
print(Back.YELLOW + "This text has a yellow background")
print(Back.CYAN + "This text has a cyan background")
# Reset everything
print(Style.RESET_ALL + "Back to normal")