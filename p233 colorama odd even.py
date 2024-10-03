import colorama
from colorama import Fore, Back, Style
# Initialize colorama
colorama.init()
for i in range(1,11):
    if i %2 ==0:
        print(Fore.RED,i,"is even")
    else:
        print(Fore.BLUE,i,"is odd")