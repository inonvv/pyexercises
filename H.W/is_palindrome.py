def is_palindrome(st):
     l = 0
    r = len(st)-1
    while l<r:
        if st[l] != st[r]:
            return False
        l = l+1
        r = r-1
    return True
print(is_palindrome("racecar"))



def isPalindrome(st):
    for i in range(int(len(st)/2)):
        high=st[len(st)-i-1]
        low=st[i]
        if high==low:
            continue
        else:
            return False
    return True



def main():
    st=input()
    print(isPalindrome(st))
main()


