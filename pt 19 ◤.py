n =int(input("Enter limit=> "))

for i in range(1,n+1):
    k=1
    for j in range(n,i-1,-1):
        print(k, end=" ")
        k=k+1
    print("")

# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1