f1=open("abc", "r")
f2=open("pqr6 'vowels print'","w")
f3=open("pqr7 'other words'","w")

list1=["a","e","i","o","u","A","E","I","O","u"]

while True:
    ch = f1.read(1)
    if not ch:
        break
    if ch in list1:
        f2.write(ch)
    else:
        f3.write(ch)

f1.close()
f2.close()
f3.close()
print("copied file 'pqr6, pqr7'")