def filter_negative(L):
    rslt=[]
    for x in L:
        if x>=0:
            rslt.append(x)
    return rslt


def twice(st):
   for i in range(1,len(st)):
       if st[i]== st[i-1]:
           return True
   return False
