import random
list1=[]
list2=[]
n1=int(input("Enter limit =>"))
for i in range(1,n1+1):
    y=random.randint(0,100)
    list1.append(y)
print(list1)

n2=int(input("Enter greater value =>"))
for x in list1:
    if x>n2:
        list2.append(x)

print(list2)