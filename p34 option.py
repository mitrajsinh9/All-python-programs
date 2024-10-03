print("press 1 for square")
print("press 2 for cube")
op=int(input("enter option=>"))

if op==1:
    no=int(input("enter no="))
    square=no*no
    print("square=",square)
elif op==2:
    no=int(input("enter no="))
    cube=no*no*no
    print("cube=",cube)
else:
    print("wrong option")