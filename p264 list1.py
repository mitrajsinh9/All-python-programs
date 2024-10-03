import random
list1=[]
list2=[]
n1 = int(input("Enter no =>"))
for i in range(1,n1+1):
    y = random.randint(1, 10)
    list1.append(y)
print(list1)

for x in list1:
    if list1.count(x)>=1 and x not in list2:
        list2.append(x)

print(list2)
