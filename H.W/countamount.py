def countAmount(lst):
    newLst=[0,0,0,0,0,0,0,0,0,0]
    for i in lst:
        newLst[i]=newLst[i]+1
    return newLst






def main():
    lst=[4,1,2,3,4,3,4,8,7,9,5,6,9,5,2,1]
    print(countAmount(lst))

main()