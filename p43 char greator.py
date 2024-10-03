print("press g for finding greater no")
print("press e for positive or negative")

op=input("enter op=")

if op=="g" or op=="G":
     no1=int(input("enter no1="))
     no2=int(input("enter no2="))

     if no1>no2:
        print("no1 is greater")
     else:
        print("no2 is greater")
elif op=="e":
     no=int(input("enter no="))
     if no>0:
         print("no is positive")
     else:
         print("no is negative")

else:
    print("wrong op")