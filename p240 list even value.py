list1=[29,32,45,40,10,50,21,20]
list2=[]

for x in list1:
    if x%2==0:
        list2.append(x)
print("list1 =",list1)
print("list2 =",list2)
x=len(list2)
print("count list2 =",x)