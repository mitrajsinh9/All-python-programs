n=int(input("Enter limit =>"))
c1=0
s1=0
c2=0
s2=0
for i in range(1,n+1):
     if i%2==0:
          print(i)
          c1=c1+1
          s1=s1+i
     else:
          print(i)
          c2=c2+1
          s2=s2+i
print("count for even=",c1,"sum for even=",s1)
print("count for even=", c2, "sum for even=", s2)