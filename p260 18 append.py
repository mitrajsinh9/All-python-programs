import random

list1=[]
list2=[]
n1 = int(input("Enter no =>"))

for i in range(1,n1+1):
    y = random.randint(1, 100)
    list1.append(y)
print(list1)

n2 = int(input("Enter no =>"))
for i in range(1,n2+1):
    y = random.randint(1, 100)
    list2.append(y)
print(list2)

print("appended:")
print(list1+list2)