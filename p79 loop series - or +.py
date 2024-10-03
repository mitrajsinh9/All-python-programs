n=int(input("enter limit=>"))
s=0
m=0
for i in range(1,n+1):
   if i %2 == 0:
       print("+",i,end=" ")
       s=s+i
   else:
       print("-",i, end=" ")
       m=m-i
print("\nSum=",s," ","minus=",m)
