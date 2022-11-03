import random
def lottery(dig1,dig2,dig3):
    winDig1=random.randint(0,9)
    winDig2=random.randint(0,9)
    winDig3=random.randint(0,9)
    print(f"the lottery number are {winDig1}-{winDig2}-{winDig3}, and your number are {dig1},{dig2},{dig3}")
    if dig1==winDig1:
        if dig2==winDig2:
            if dig3==winDig3:
                return True
    return False

def main():
    print("choose 3 numbers and try to win the lottery")
    dig1=int(input())
    dig2=int(input())
    dig3=int(input())
    didWin=lottery(dig1,dig2,dig3)
    if didWin:
        print("YOU WIN!")
    else:
        print("YOU LOSE! :(")
main()
