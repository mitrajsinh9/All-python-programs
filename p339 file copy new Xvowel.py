f1 = open("abc", "r")
f2=open("pqr3 'no vowels'","w")
list1=["a","e","i","o","u","A","E","I","O","u"]
while True:
    ch = f1.read(1)
    if not ch:
        break
    if ch in list1:
        pass
    else:
        f2.write(ch)

f1.close()
f2.close()
print('copied file "pqr3"')