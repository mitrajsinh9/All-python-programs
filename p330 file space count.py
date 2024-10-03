f1=open("abc","r")
c=0
while True:
    ch=f1.read(1)
    if not ch:
        break
    if ch==" ":
        c+=1
f1.close()
print("Total spaces are",c)
"""
1) vowels count ?
2) u/l count ?
3) u->l l->u
4) vowelsX
5) uppX
6) space X
"""