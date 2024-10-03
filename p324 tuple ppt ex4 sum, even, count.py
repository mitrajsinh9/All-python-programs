#4) Print Sum of even and Count also

t1=(50,5,7,9,20,95,36)
s=0
c=0

print("Even no:")
for i in t1:
    if i%2==0:
        print(i)
        s=s+i
        c+=1
print("Sum:",s,"\t","Count:",c)