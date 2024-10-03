n=int(input("enter limit=>"))
s=0
for i in range(1,n+1):
    print(i,end="+1/")
    s=s+1/i
print("\nsum=",s)
