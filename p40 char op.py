print("press a for square")
print("press b for cube")
op=input("enter option=>")

if op=="a" or op=="A":
    no=int(input("enter no="))
    square=no*no
    print("square=",square)
elif op=="b" or op=="B":
    no=int(input("enter no="))
    cube=no*no*no
    print("cube=",cube)
else:
    print("wrong option")