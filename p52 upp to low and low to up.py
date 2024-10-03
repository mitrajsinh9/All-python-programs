print("enter any letter to upper to lower and lower to upper")
letter=input("enter a letter=")
if letter.isupper():
    print(letter.lower())
elif letter.islower():
    print(letter.upper())
else:
    print(letter)
