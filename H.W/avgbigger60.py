def avg_grade(lst):
    fail = len(lst)
    sum = 0
    for x in lst:
        if x < 60:
            fail = fail - 1
        else:
            sum = sum + x

    return sum / fail