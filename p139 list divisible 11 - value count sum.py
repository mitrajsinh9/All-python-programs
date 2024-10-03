list1=[55,9,10,23,45,11,9,8,33,11,12,44,45,11,100]
c=0
t=0
for x in list1:
    if x%11==0:
        print(x)
        c+=1
        t+=x
print("total = ",t," Count = ",c)