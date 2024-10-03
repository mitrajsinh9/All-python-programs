#7) Print 11 -22 33 -44 55 in reverse -11 22 -33 44 -55 Print in reverse mode


tuple1=(1,2,3,4,5,6,7,8,9)
list1=list(tuple1)
list1.reverse()
tuple1=tuple(list1)
print(tuple1)