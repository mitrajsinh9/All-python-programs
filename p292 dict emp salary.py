import random

d1 = {}
n = int(input("Enter limit:=>"))

for i in range(1, n + 1):
    k = i
    v = random.randint(10000, 50000)
    d1[k] = v

print("Empno\tSalary\t\tStatus")
print("-"*30)
for k,v in d1.items():
    if v<15000:
        print(k,"\t\t",v,"\t\tDo ur best")
    else:
        print(k,"\t\t",v,"\t\tKeep it up")
print("-"*30)