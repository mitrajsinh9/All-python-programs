import random
for i in range(1,6):
    x=random.randint(1,50)
    y=random.randint(1,50)
    print("No1 = ",x, " No2 =  ",y)
    z=x+y
    n=int(input("enter correct answer :"))
    if n==z:
        print("answer is right")
    else:
        print("answer is wrong")
