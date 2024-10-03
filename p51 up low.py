print("enter any letter to find out if letter is a upper or lower")
letter=input("enter a letter=")
if letter.isupper():
    print("upper")
elif letter.islower():
    print("lower")
else:
    print("other")