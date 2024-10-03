import colorama
from colorama import Fore, Back, Style
# Initialize colorama
colorama.init()

marks=int(input("Enter ur math marks =>"))

if marks >= 18:
    print(Fore.BLUE,"pass")
else:
    print(Fore.RED,"fail")