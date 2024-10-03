t1 = (50, 5, 7, 9, 20, 35, 36)
c1=0
c2=0
for x in t1:
    if x % 2 == 0:
        print(x, "is even")
        c1+=1
    else:
        print(x, "is odd")
        c2+=1
print("total count of even=",c1)
print("total count of odd=",c2)