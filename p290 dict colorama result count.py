import colorama
from colorama import Fore, Back, Style
colorama.init()
import random

d1 = {}
n = int(input("Enter limit:=>"))

for i in range(1, n + 1):
    k = i
    v = random.randint(1, 50)
    d1[k] = v
c1=0
c2=0
print("No\tMarks\tResult") #\t for 5 space, \n for new
print("*"*30)
for k,v in d1.items():
    if v>18:
        print(k,"\t",v,"\t",Fore.BLUE,"pass")
        c1+=1

    else:
        print(k,"\t",v,"\t",Fore.RED,"fail")
        c2+=1

print("*"*30)
print("Pass count:",c1)
print("Fail count:",c2)