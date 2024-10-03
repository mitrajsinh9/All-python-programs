d1={11:12000,13:14000,15:2000,16:30000,17:20000,18:21000}
print("Empno\tSalary\tStatus")
print("*"*30)
for k,v in d1.items():
    if v<15000:
        print(k,"\t",v,"\tGood")
print("*"*30)