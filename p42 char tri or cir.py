print("press v for area of tri")
print("press o for area of cir")
op=input("enter option=")

if op=="v" or op=="V":
    b=int(input("enter base"))
    h=int(input("enter height"))
    area=0.5*b*h
    print("area of triangle=",area)
elif op=="o" or op=="O":
    r=int(input("enter radius="))
    area=3.14*r*r
    print("area of circle=",area)
else:
    print("wrong op")