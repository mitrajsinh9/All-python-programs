bill1=0
bill2=0
while True:
    print("press 1 for pizza")
    print("press 2 burger")
    print("press 3 for quit")
    op=int(input("Enter op:"))
    if op==1:
        print("price for pizza=499")
        qty=int(input("Enter qty:"))
        bill1=499*qty
        print("bill=",bill1)
    elif op==2:
        print("price for burger=200")
        qty=int(input("Enter qty:"))
        bill2=200*qty
        print("bill=",bill2)
    elif op==3:
        print("grand total=",bill1+bill2)
        break
    else:
        print("wrong op")