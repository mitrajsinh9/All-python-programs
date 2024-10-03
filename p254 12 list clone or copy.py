import random
list1=[]
list2=[]
n=int(input("Enter limit =>"))
for i in range(1,n+1):
    y=random.randint(0,100)
    list1.append(y)
list2=list1
print(list1)
print(list2)