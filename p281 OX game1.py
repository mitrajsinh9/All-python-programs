list1 = ['_', '_', '_', '_', '_', '_', '_', '_', '_']

turn = 1

while turn < 10:
    if turn % 2 == 0:
        pos=int(input("Mitraj enter ur turn:"))
        list1[pos-1]="X"
    else:
        pos=int(input("Vraj enter ur turn:"))
        list1[pos-1]="O"

    print("Turn = ", turn)
    print("|",list1[0], "|", list1[1], "|", list1[2], "|", )
    print("|",list1[3], "|", list1[4], "|", list1[5], "|", )
    print("|",list1[6], "|", list1[7], "|", list1[8], "|")
    turn=turn+1