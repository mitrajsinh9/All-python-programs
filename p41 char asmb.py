print("press + for addition")
print("press - for subtarction")
print("press * for multiple")
print("press / for division")
op=input("enter option=>")

if op=="+":
    no1=int(input("enter no="))
    no2=int(input("enter no="))
    addition=no1+no2
    print("addition=",addition)
elif op=="-":
    no1=int(input("enter no="))
    no2=int(input("enter no="))
    subtraction=no1-no2
    print("subtraction=",subtraction)
elif op=="*":
    no1=int(input("enter no="))
    no2=int(input("enter no="))
    multiple=no1*no2
    print("multiple=",multiple)
elif op=="/":
    no1=int(input("enter no="))
    no2=int(input("enter no="))
    division=no1/no2
    print("division=",division)
else:
    print("wrong no")