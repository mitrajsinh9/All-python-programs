import random
list1=[]

n=int(input("Enter limit =>"))
for i in range(1,n+1):
    y=random.randint(0,100)
    list1.append(y)
print(list1)

a=list1[0]
b=list1[-1]
c=a+b
print("first nd last value add =>",c)