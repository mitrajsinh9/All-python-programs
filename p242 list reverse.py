import random
list1=[]
n=int(input("Enter limit =>"))
for i in range(1,n+1):
    y=random.randint(0,20)
    list1.append(y)

print(list1)
list1.reverse()
print(list1)