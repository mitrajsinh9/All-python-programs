import random

c1=0
c2=0
z=0

for i in range(1, 6):
        x = random.randint(1, 50)
        y = random.randint(1, 50)
        op = random.randint(1, 4)
        print("No1 =", x,  " No2 =", y)
        if op==1:
            z = x + y
            n = int(input("Enter addition of above: "))
        elif op==2:
            z = x - y
            n = int(input("Enter subtraction of above: "))
        elif op==3:
            z = x * y
            n = int(input("Enter multiple of above: "))
        elif op==4:
            z = x / y
            n = int(input("Enter divided of above: "))

        if n == z:
            print("Correct")
            c1 = c1 + 1
        else:
            print("Incorrect")
            c2 = c2 + 1

print("count of Correct answers:", c1)
print("count of Incorrect answers:", c2)