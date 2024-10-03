while True:
    print("press 1 for area of tri")
    print("press 2 for area of cir")
    print("press 3 for quit")
    op=input("enter option=")

    if op=="1":
        b=int(input("enter base"))
        h=int(input("enter height"))
        area=0.5*b*h
        print("area of triangle=",area)
    elif op=="2":
        r=int(input("enter radius="))
        area=3.14*r*r
        print("area of circle=",area)
    elif op=="3":
        break
    else:
        print("wrong op")