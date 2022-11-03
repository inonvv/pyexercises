chosenNumber=int(input("enter chosen number"))## how do i disapear the decimal
secondNumber=0
newNumber=0
if chosenNumber<10 and 100>chosenNumber:
    print("wrong number please try again!")
if chosenNumber > 10 and chosenNumber <100 :
    secondNumber=chosenNumber%10
    secondNumber=secondNumber+2
    chosenNumber=chosenNumber//10
    newNumber=(chosenNumber+2)+secondNumber
    print(secondNumber,"second number")
    print(chosenNumber,"chosen number")
    print(newNumber,"newNumber")def cal_dis(v1,t1,v2,t2):
    t1=t1/60
    t2=t2/60
    train1=v1*t1
    train2=v2*t2
    if train1>train2:
        totaldis=train1-train2
    else:
        totaldis=train2-train1
    return totaldis



def main():

    print(cal_dis(90,30,120,20))
main()





import math


def pointsdis(x1,y1,x2,y2):
    D=math.sqrt(((x1-x2)**2)+((y1-y2)**2))

    return D
def main():
    x1=float(input("x1"))
    y1=float(input("y1"))
    x2=float(input("x2"))
    y2=float(input("y2"))
    print(pointsdis(x1,y1,x2,y2))

main()

