def printBoard(line1,line2,line3):
    print(line1)
    print(line2)
    print(line3)

def choose(line1,line2,line3):
    print("input selected numbers to play the game")
    for i in range (len(line1)):
        line1[i]=int(input(f"put number in place {line1[i]}"))
        line2[i]=int(input(f"put number in place {line2[i]}"))
        line3[i]=int(input(f"put number in place {line3[i]}"))
    return line1,line2,line3
def checkSum(a,b,c):
    if a+b+c==15:
        return True
    else:
        return False

def checklines(line1,line2,line3):
    row1=checkSum(line1[0],line1[1],line1[2])
    row2=checkSum(line2[0],line2[1],line2[2])
    row3=checkSum(line3[0],line3[1],line3[2])
    if row1 and row2 and row3:
        return True
    else:
        return False

def checkColumns(line1,line2,line3):
    Columns1=checkSum(line1[0],line2[0],line3[0])
    Columns2=checkSum(line1[1],line2[1],line3[1])
    Columns3=checkSum(line1[2],line2[2],line3[2])
    if Columns1 and Columns2 and Columns3:
        return True
    else:
        return False
def checkDiagonal(line1,line2,line3):
    diagonal1=checkSum(line1[0],line2[1],line3[2])
    diagonal2=checkSum(line1[2],line2[1],line3[0])
    if diagonal1 and diagonal2:
        return True
    else:
        return False
def main():
    line1 = [1, 2, 3]
    line2 = [4, 5, 6]
    line3 = [7, 8, 9]
    print("welcome to assafGay game!")
    print("please insert numbers by columns and try to reach 15 and win the game!")
    printBoard(line1,line2,line3)
    line1,line2,line3=choose(line1,line2,line3)
    printBoard(line1,line2,line3)
    if checklines(line1,line2,line3) and checkColumns(line1,line2,line3) and checkDiagonal(line1,line2,line3):
        print("SUCCESS YOU  ARE NOW KING OF GAYASSAF")
    else:
        print("TOO BAD YOU ARE NOT GAYASSAF :(")

main()