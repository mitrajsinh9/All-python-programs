n=int(input("Enter a limit: "))

for i in range(1,n+1):
    for j in range(n,i-1,-1):
        print(i,end=" ")
    print("")

# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5