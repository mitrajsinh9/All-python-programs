n=int(input("enter a no:"))
c=0
s=0
for i in range (1,n+1):
    if i %2 == 0:
        print(i)
        c=c+1
        s=s+i
print("count=",c,"sum=",s)