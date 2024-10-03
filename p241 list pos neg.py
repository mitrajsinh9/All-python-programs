import random
list1=[]
list2=[]
list3=[]
n=int(input("Enter limit =>"))
for i in range(1,n+1):
    y=random.randint(-20,20)
    list1.append(y)

for x in list1:
    if x>0:
        list2.append(x)
    else:
        list3.append(x)

print(list1)
print("pos=",list2)
print("neg=",list3)
x=len(list2)
print("count pos =",x)
x=len(list3)
print("count neg =",x)