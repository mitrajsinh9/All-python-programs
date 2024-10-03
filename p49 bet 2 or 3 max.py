print("press m for max no bet 2")
print("press n for max no bet 3")

op=int(input("enter option="))

if op==1:
    no1=int(input("enter no1="))
    no2=int(input("enter no2="))

    if no1>no2:
        print("no1 is maximum")
    elif no2>no1:
        print("no2 is maximum")

elif op==2:
    no1 = int(input("enter no1="))
    no2 = int(input("enter no2="))
    no3 = int(input("enter no3="))

    if no1>=no2 and no1>=no3 :
        print("no1 is maximum")
    elif no2>=no1 and no2>=no3:
        print("no2 is maximum")
    else:
        print("no3 is maximum")

else:
    print("wrong option")