print("press 1 for xerox")
print("press 2 for type")
print("press 3 for both")

op=int(input("enter option=>"))

if op==1:
    copy=int(input("enter copy no="))
    if copy >= 50:
         print("per copy price 5")
         print("bill = ", copy * 5)
    else:
         print("per copy price 7")
         print("bill =", copy * 7)

elif op==2:
    type=int(input("enter type no"))

    if type >= 50:
        print("per type price 15")
        print("bill =",type*15)
    else:
        print("per type no 20")
        print("bill=", type*20)

elif op==3:
    copy1=int(input("enter copy no="))
    pages1=int(input("enter pages="))

    if copy1 >= 50:
        copy1=5
        print("per copy price 5")
        print("bill1 = ", copy1 * 5)
        bill1=copy1*5
    else:
        copy1=7
        print("per copy price 7")
        print("bill1 =", copy1 * 7)
        bill1=copy1*7
    if pages1 >= 50:
        type=15
        print("per page price=15")
        print("bill2=",pages1*15)
        bill2=pages1*15
    else:
        type=20
        print("per page price=20")
        print("bill2=",pages1*20)
        bill2=pages1*20
        print("grand total=",bill1+bill2)

else:
    print("wrong option")