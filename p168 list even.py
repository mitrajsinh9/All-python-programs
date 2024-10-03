import random
list1=[]
n=int(input("Enter limit =>"))
for i in range(1,n+1):
    y=random.randint(1,50)
    list1.append(y)

print(list1)

for x in list1:
    if x%2==0:
        print(x)