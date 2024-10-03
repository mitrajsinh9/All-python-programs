list1=[55,9,10,23,45,11,9,8,33,11,12,44,45,11,100]
list2=[]
for x in list1:
    if x % 5==0:
        list2.append(x)

print(list2)
print(list1)