list1=["a","b","c","d","E","m","H","i","T"]
c1=0
c2=0
for x in list1:
    if x.isupper():
        print(x,"is upper")
        c1+=1
print("count for upper=",c1)