print("press 1 for next no")
print("press 2 for previous no")

op=int(input("enter op="))

if op==1:
    no=int(input("enter no="))
    print("next no=",no+1)

elif op==2:
    no=int(input("enter no="))
    print("next no=",no-1)

else:
    print("wrong op")