n=int(input("Enter limit: "))

for i in range(1,n+1):
    for j in range(n,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print(j,"",end="")
    print("")
