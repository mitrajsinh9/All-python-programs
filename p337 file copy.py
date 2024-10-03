f1=open("abc","r")
f2=open("pqr 'copy file abc'","w")
while True:
    ch=f1.read(1)
    if not ch:
        break
    f2.write(ch)
f1.close()
f2.close()
print("copied file 'pqr'")
"""
1)1->2 , space X
2)1->2 . vowel X
3)1->2      upper
    ->3     lower
4)1->2  vowl
    ->3 other
5) 1->2 vowel 7


"""