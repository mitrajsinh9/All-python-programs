n=int(input("enter limit=:"))
m=0
for i in range(n,0,-1):
    print(i,end=" * ")
    m = m + i * i
print("\nmul=", m)