n=int(input("Enter limit: "))

for i in range(1,n+1):
    k = n-i+1
    for j in range(n,i,-1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(k,end=" ")
        k=k+1
    print("")

#         5
#       4 5
#     3 4 5
#   2 3 4 5
# 1 2 3 4 5