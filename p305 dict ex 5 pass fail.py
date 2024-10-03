#Q.5 Write a Python script to print data in vertical form and also display whether that student
#     is pass or not from dicitionary. (18 marks pass)


marks={"ram":33,"rahul":15,"devesh":30,"jayul":34,"jiya":16,"sadhana":11}

print("No\tMarks\tResult")
print("*"*30)
for k,v in marks.items():
    if v>18:
        print(k,"\t",v,"\tpass")
    else:
        print(k,"\t",v,"\tfail")
print("*"*30)