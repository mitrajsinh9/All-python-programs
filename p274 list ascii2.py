import random

l1=[]
n=int(input("Enter a number: "))
for i in range(1,n+1):
    y=random.randint(97,122)
    l1.append(chr(y))

print(l1)
print("\n\n")
c1 = 0
c2 = 0
for x in l1:

    if x=="a" or x=="e" or x=="i" or x=="o" or x=="u":
        print(x,"is vowel")
        c1=c1+1
    else:
        print(x,"is consonant")
        c2=c2+1
print("count of vowels=",c1)
print("count of consonants=",c2)