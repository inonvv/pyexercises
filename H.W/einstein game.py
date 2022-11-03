def albertino():
    print("welcome to the einstien magic game!")
    print("please enter a 3 digits number who is positive and the fist and last numbers are different")
    num=int(input(":"))
    if num<100  or num>999:

        return print("please follow the instruction above")
    firstNum=num/100
    lastNum=num%10
    if firstNum==lastNum:
        return "the first and last digits should be different!"

    reverse = int(str(num)[::-1])
    finalNum=num-reverse

    # if finalNum < 0:
    #     finalNum = finalNum *-1

    finalNum = finalNum if finalNum > 0 else -finalNum

    print("the number is",num,"the difference is",finalNum)
    if finalNum<100:
        differencerev=finalNum*10
    else:
        differencerev=int(str(finalNum)[::-1])
    print("the riverse differce is",differencerev)
    if finalNum+differencerev==1089:
        return "SUCCEEDED"
    else:
        return "FALIED"

def main():
    print(albertino())
main()




