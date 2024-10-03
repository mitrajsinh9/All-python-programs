print("press 1 for finding greater no")
print("press 2 for positive or negative")

op=int(input("enter op="))

if op==1:
     no1=int(input("enter no1="))
     no2=int(input("enter no2="))

     if no1>no2:
        print("no1 is greater")
     else:
        print("no2 is greater")
elif op==2:
     no=int(input("enter no="))
     if no>0:
         print("no is positive")
     else:
         print("no is negative")

else:
    print("wrong op")