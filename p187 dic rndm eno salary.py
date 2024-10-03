import random
d1={}
n=int(input("Enter limit =>"))
for i in range(1,n+1):
    d1[i]=random.randint(10000,50000)
print("Eno\tSalary")
print("*"*30)
for k,v in d1.items():
    print(k,"\t",v)