import random
op=random.randint(1,4)
c1=0
c2=0

if op==1:
    for i in range(1,6):
        x=random.randint(1,50)
        y=random.randint(1,50)
        print("No1 = ",x, " No2 =  ",y)
        z=x+y
        n=int(input("enter correct answer of addtion :"))
        if n==z:
            print("answer is right")
            c1=c1+1
        else:
            print("answer is wrong")
            c2=c2+1

    print("right answers :",c1)
    print("wrong answers :",c2)



elif op==2:
    for i in range(1,6):
        x=random.randint(1,50)
        y=random.randint(1,50)
        print("No1 = ",x, " No2 =  ",y)
        z=x-y
        n=int(input("enter correct answer of subtraction :"))
        if n==z:
            print("answer is right")
            c1=c1+1
        else:
            print("answer is wrong")
            c2=c2+1

    print("right answers :",c1)
    print("wrong answers :",c2)

elif op==3:
    for i in range(1,6):
        x=random.randint(1,50)
        y=random.randint(1,50)
        print("No1 = ",x, " No2 =  ",y)
        z=x*y
        n=int(input("enter correct answer of multiple :"))
        if n==z:
            print("answer is right")
            c1=c1+1
        else:
            print("answer is wrong")
            c2=c2+1

    print("right answers :",c1)
    print("wrong answers :",c2)

elif op==4:
    for i in range(1,6):
        x=random.randint(1,50)
        y=random.randint(1,50)
        print("No1 = ",x, " No2 =  ",y)
        z=x/y
        n=int(input("enter correct answer of division :"))
        if n==z:
            print("answer is right")
            c1=c1+1
        else:
            print("answer is wrong")
            c2=c2+1

    print("right answers :",c1)
    print("wrong answers :",c2)

else:
    print("wrong option")

