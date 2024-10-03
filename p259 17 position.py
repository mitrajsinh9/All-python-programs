import random

list1 = []
n1 = int(input("Enter no =>"))
for i in range(1, n1 + 1):
    y = random.randint(1, 100)
    list1.append(y)

print(list1)

n2=int(input("enter position =>"))
n3=int(input("enter value =>"))
list1.insert(n2,n3) #pos, value

print(list1)

#enter position value