print("press 1 for pizza")
print("press 2 for dosa")
print("press 3 for burger")

op=int(input("enter option="))

if op==1:
    pizza=499
    print("pizza price =",pizza)
    qty=int(input("Enter qty =>"))
    print("bill of pizza = ",pizza*qty)
elif op==2:
    dosa=399
    print("dosa price=",dosa)
    qty = int(input("Enter qty =>"))
    print("bill of dosa=",dosa*qty)
elif op==3:
    burger=299
    print("burger price=",burger)
    qty = int(input("Enter qty =>"))
    print("bill of burger=",burger*qty)
else:
    print("wrong optiom")
