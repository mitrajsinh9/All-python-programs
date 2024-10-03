list=[]
n=int(input("Enter number of value you want to enter=> "))
for i in range(n):
    a=int(input("Enter {i+1} value=> "))
    list.append(a)

for i in list:
    if i > 33:
        print(i)