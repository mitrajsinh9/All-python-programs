f1=open("abc","r")
c1=0
c2=0
while True:
    ch=f1.read(1)
    if not ch:
        break
    if ch.isupper():
        c1+=1
    elif ch.islower():
        c2+=1
f1.close()
print("Count of upper = ",c1)
print("Count of lower = ",c2)