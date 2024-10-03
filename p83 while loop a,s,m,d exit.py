while True:
    print("press 1 for addition")
    print("press 2 for subtraction")
    print("press 3 for multiple")
    print("press 4 for division")
    print("press 5 for quit")
    op=int(input("enter option=>"))

    if op==1:
        no1=int(input("enter no="))
        no2=int(input("enter no="))
        addition=no1+no2
        print("addition=",addition)
    elif op==2:
        no1=int(input("enter no="))
        no2=int(input("enter no="))
        subtraction=no1-no2
        print("subtraction=",subtraction)
    elif op==3:
        no1=int(input("enter no="))
        no2=int(input("enter no="))
        multiple=no1*no2
        print("multiple=",multiple)
    elif op==4:
        no1=int(input("enter no="))
        no2=int(input("enter no="))
        division=no1/no2
        print("division=",division)
    elif op==5:
        break
    else:
        print("wrong no")