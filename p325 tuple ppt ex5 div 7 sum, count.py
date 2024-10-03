#5) Display only numbers divisible by 7 , count and sum it

t1=(50,5,7,9,21,95,35)
s=0
c=0

print("Div 7 no's:")
for i in t1:
    if i%7==0:
        print(i)
        s=s+i
        c+=1
print("Sum:",s,"\t","Count:",c)