import webbrowser

print("google")
print("digiprimestudio")
print("youtube")
print("instagram")
print("break")
print("")

op=(input("enter website=>"))

if op == "google":
    webbrowser.open("www.google.com")
elif op =="digiprimestudio":
    webbrowser.open("www.digiprimestudio.com")
elif op =="youtube":
    webbrowser.open("www.youtube.com")
elif op =="instagram":
    webbrowser.open("www.instagram.com")
else:
    print("wrong website")