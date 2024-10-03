f1=open("abc", "r")
f2=open("pqr8 'print vowels at 7'","w")
list1=["a","e","i","o","u","A","E","I","O","U"]
while True:
    ch = f1.read(1)
    if not ch:
        break
    if ch in list1:
        f2.write("7")
    else:
        f2.write(ch)

f1.close()
f2.close()
print('copied file "pqr8"')