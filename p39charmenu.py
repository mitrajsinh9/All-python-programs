print("press n for next no")
print("press @ for previous no")

op=input("enter op=")

if op=="n" or op=="N":
    no=int(input("enter no="))
    print("next no=",no+1)

elif op=="@":
    no=int(input("enter no="))
    print("next no=",no-1)

else:
    print("wrong op")