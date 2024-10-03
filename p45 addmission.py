print("press 1 for BCA")
print("press 2 for MCA")
print("press 3 for BSC")
print("press 4 for MSC")

op=int(input("enter option=>"))

if op==1:
    BCA=60000
    print("BCA fees =",BCA)
    qty=int(input("Enter no of student =>"))
    print("total fees of student = ",BCA*qty)
elif op==2:
    MCA = 90000
    print("MCA fees=", MCA)
    qty = int(input("Enter no of student =>"))
    print("total fees of student=", MCA * qty)
elif op==3:
    BSC = 70000
    print("BSC fees=", BSC)
    qty = int(input("Enter no of student =>"))
    print("total fees of student=", BSC * qty)
elif op==4:
    MSC = 110000
    print("MSC fees=", MSC)
    qty = int(input("Enter no of student =>"))
    print("total fees of student=", MSC * qty)
else:
    print("wrong optiom")
