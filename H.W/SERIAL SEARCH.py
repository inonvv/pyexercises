def search(L, x):
    for e in L:
        if e == x:
            return True
    return False


lst = [4, 7, 2, 3, 1]
result = search(lst, 8)
print(result)


def search_cnt(L, x):
    count = 0
    for e in L:
        count = count + 1
        if e == x:
            return count  # <-- change!
    # if we got here the search failed
    return count  # <-- change!

