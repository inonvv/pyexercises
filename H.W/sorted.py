def sorting(lst):
    lst=sorted(lst)
    return lst
def main():
    lst=[5,0,4,50,9,1,3,4,65,7]
    print(sorting(lst))
main()


L= [21,435,56,2,7,789,34,65]

for a in range(len(L)):
    for b in range(0, len(L)-a-1):
        if(L[b]>L[b+1]):
            L[b],L[b+1]=L[b+1],L[b]