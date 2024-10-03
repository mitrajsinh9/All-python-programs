import random
x=random.randint(1,50)
y=random.randint(1,50)
print(x," ",y)
z=x+y
n=int(input("enter correct answer :"))
if n==z:
    print("answer is right")
else:
    print("answer is wrong")
