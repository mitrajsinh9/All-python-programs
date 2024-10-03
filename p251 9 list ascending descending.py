import random
list1=[]

n=int(input("Enter limit =>"))
for i in range(1,n+1):
    y=random.randint(0,100)
    list1.append(y)
print(list1)

list1.sort()
print("ascending =",list1)
list1.reverse()
print("descending =",list1)