import random
list1=[]
n=int(input("Enter limit =>"))
for i in range(1,n+1):
    y=random.randint(-20,20)
    list1.append(y)

print(list1)

for x in list1:
    if x>0:
        print(x,"pos")
    else:
        print(x,"neg")


