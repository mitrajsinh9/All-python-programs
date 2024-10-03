import random
list1=[]
n=int(input("Enter limit =>"))
for i in range(1,n+1):
    y=random.randint(0,50)
    list1.append(y)

print(list1)
print("max = ",max(list1))
print("min =",min(list1))
print("lenth=",len(list1))
print("sum =",sum(list1))
