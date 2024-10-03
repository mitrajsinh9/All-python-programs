# Q8. Write a Python program to remove a key from a dictionary.

marks={"ram":33,"rahul":15,"devesh":30,"jayul":34,"jiya":16,"sadhana":11}

k=input("Emter key want to remove:>")

if k in marks.keys():
    marks.pop(k)
print(marks)