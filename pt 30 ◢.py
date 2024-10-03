n=int(input("Enter limit: "))

for i in range(1,n+1):
    k = i
    for j in range(n,i,-1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(k,end=" ")
        k=k-1
    print("")

#         1
#       2 1
#     3 2 1
#   4 3 2 1
# 5 4 3 2 1