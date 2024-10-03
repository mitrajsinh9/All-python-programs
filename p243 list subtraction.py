import random
list1=[]
list2=[]
n1=int(input("Enter limit =>"))
for i in range(1,n1+1):
    y=random.randint(0,50)
    list1.append(y)

n2=int(input("Enter limit =>"))
for i in range(1,n2+1):
    y=random.randint(0,50)
    list2.append(y)

print(list1)
print("list1 max = ",max(list1))
print(list2)
print("list2 max = ",max(list2))
print('')
sub=(max(list1)-max(list2))
print("SUB of l1 nd l2 =",sub)