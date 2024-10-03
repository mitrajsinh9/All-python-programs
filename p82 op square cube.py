while True:
     print("press 1 for square")
     print("press 2 for cube")
     print("press 3 for quit")
     op=int(input("enter option==>"))
     if op==1:
          n=int(input("enter no=>"))
          square=n*n
          print("square=",square)
     elif op==2:
          n=int(input("enter no=>"))
          cube=n*n*n
          print("cube=",cube)
     elif op==3:
           break
     else:
          print("wrong no")