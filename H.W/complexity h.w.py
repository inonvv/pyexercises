import time

def f1(n):
    s = 0
    for i in range(n):
        s = s + i
    return s

def f2(n):
    s = 0
    for i in range(n):
        for j in range(n):
            s = s + (i + j)
    return s


start = time.clock()
f2(1000)
end = time.clock()
print("n = 1000, measured time:", end-start)

start = time.clock()
f2(2000)
end = time.clock()
print("n = 2000, measured time:", end-start)

start = time.clock()
f2(4000)
end = time.clock()
print("n = 4000, measured time:", end-start)




def poli()
    lst=st
    l=0
    r=len(st)-1
    while l<r
        if lst[l] != lst[r]:
            return False
        l=l+1
        r=r-1
        return True
