import random

l1=[]
n=int(input("Enter a number: "))
for i in range(1,n+1):
    y=random.randint(97,122)
    l1.append(chr(y))
print(l1)