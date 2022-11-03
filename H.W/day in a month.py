def month_days(num):
    month=[0,31,29,31,30,31,30,31,31,30,31,30,31]
    if num>1 and num<13:
        return month[num]
    else:
        return -1num=int(input())
print(month_days(num))