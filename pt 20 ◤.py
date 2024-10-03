n =int(input("Enter limit=> "))
k=n
for i in range(1,n+1):
    for j in range(n,i-1,-1):
        print(k, end=" ")
    k=k-1
    print("")

# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1