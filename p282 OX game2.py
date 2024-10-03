list1 = ['_', '_', '_', '_', '_', '_', '_', '_', '_']

turn = 1

while turn < 10:
    if turn % 2 == 0:
        pos=int(input("Mitraj enter ur turn:"))
        list1[pos-1]="O"
    else:
        pos=int(input("Vraj enter ur turn:"))
        list1[pos-1]="X"

    print("Turn = ", turn)
    print("|",list1[0], "|", list1[1], "|", list1[2], "|",)
    print("|",list1[3], "|", list1[4], "|", list1[5], "|",)
    print("|",list1[6], "|", list1[7], "|", list1[8], "|")
    turn=turn+1

    if list1[0]==list1[1]==list1[2]:
        if list1[0]=="O":
            print("Mitraj is winner")
        elif list1[0]=="X":
            print("Vraj is winner")
    elif list1[3]==list1[4]==list1[5]:
        if list1[3]=="O":
            print("Mitraj is winner")
        elif list1[3]=="X":
            print("Vraj is winner")
    elif list1[6]==list1[7]==list1[8]:
        if list1[6]=="O":
            print("Mitraj is winner")
        elif list1[6]=="X":
            print("Vraj is winner")
    elif list1[0]==list1[4]==list1[8]:
        if list1[0]=="O":
            print("Mitraj is winner")
        elif list1[0]=="X":
            print("Vraj is winner")
    elif list1[2]==list1[4]==list1[6]:
        if list1[2]=="O":
            print("Mitraj is winner")
        elif list1[2]=="X":
            print("Vraj is winner")
    elif list1[0]==list1[3]==list1[6]:
        if list1[0]=="O":
            print("Mitraj is winner")
        elif list1[0]=="X":
            print("Vraj is winner")
    elif list1[1]==list1[4]==list1[7]:
        if list1[1]=="O":
            print("Mitraj is winner")
        elif list1[1]=="X":
            print("Vraj is winner")
    elif list1[2]==list1[5]==list1[8]:
        if list1[2]=="O":
            print("Mitraj is winner")
        elif list1[2]=="X":
            print("Vraj is winner")