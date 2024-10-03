print("press s for square")
print("press @ for cube")
op=input("enter option=>").lower()
if op=="s":
    no=int(input("enter no=>"))
    square=no*no
    print("square=",square)
elif op=="@":
    no=int(input("enter no=>"))
    cube=no*no*no
    print("cube=",cube)
else:
    print("wrong option")