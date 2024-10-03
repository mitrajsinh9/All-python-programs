def add():
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    print("add = ",a+b)

def max2():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    if a>b:
        print("Max is=",a)
    else:
        print("Max is=",b)

def tab():
    n = int(input("Enter number =>"))
    for i in range(1, 11):
        print(n, "*", i, "=", n * i)

def oddeven():
    n = int(input("Enter limit =>"))
    if n % 2 == 0:
        print("even")
    else:
        print("odd")


def posneg():
    no = int(input("enter no="))

    if no > 0:
        print("no is possitive")
    else:
        print("negative")


def areaoftri():
    b=int(input("enter base:>"))
    h=int(input("enter hight:>"))
    area=0.5*b*h
    print("area=",area)


def areaofcricle():
    r=int(input("enter radius:>"))
    area=3.14*r*r
    print("area=",area)


def max3():
    a=int(input("Enter first number:>"))
    b=int(input("Enter second number:>"))
    c=int(input("Enter third number:>"))
    if a>b and a>c:
        print("Max is=",a)
    elif b>a and b>c:
        print("Max is=",b)
    else:
        print("Max is=",c)


def cube():
    n=int(input("Enter no:>"))
    cube=n*n*n
    print("cube=",cube)


add()
max2()
tab()
oddeven()
posneg()
areaoftri()
areaofcricle()
max3()
cube()



"""
addition()
maximum()
table()
oddeven()
posneg()
areaoftri()
areaofcricle()
max3()
cube()

"""