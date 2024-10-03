f1 = open("abc", "r")

list1=["a","e","i","o","u","A","E","I","O","U"]
while True:
    ch = f1.read(1)
    if not ch:
        break
    if ch in list1:
        pass
    else:
        print(ch, end="")

f1.close()
