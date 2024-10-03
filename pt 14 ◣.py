n =int(input("Enter limit => "))
k=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(k, end=" ")
        k=k+1
    print("")

# 5
# 4 4
# 3 3 3
# 2 2 2 2
# 1 1 1 1 1