n=int(input("enter a number:"))
c=0
s=0
for i in range (1,21):
    if i %3 == 0:
        print(i)
        c=c+1
        s=s+i
print("count=",c,"sum =",s)