 max5(a, b, c, d):
    # delete pass and fill in your code below
    if a > b and a > c and a > d:
        return a
    elif b > a and b > c and b > d:
        return b
    elif c > a and c > b and c > d:
        return c
    else:
        return d

def max2(a, b):
		if a > b:			return a
		else:
			return b

	def max3(a, b, c):
		max_a_b = max2(a, b)
		max_all = max2(max_a_b, c)
		return max_all

	def max4_v1(a, b, c, d):
		max_a_b_c = max3(a, b, c)
		max_all = max2(max_a_b_c, d)
		return max_all

	max4_v1(7,13,0,42)
def max2(a, b):
2	    if a > b:
3	        return a
4	    else:
5	        return b
6
7	def max3_v3(a,b,c):
8	    max_a_b = max2(a,b)
9	    max_all = max2(max_a_b, c)
10	    return max_all
11
12	def max10(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10):
13	    x = max3_v3(a1, a2, a3)
14	    y = max3_v3(a4, a5, a6)
15	    z = max3_v3(a7, a8, a9)
16	    max_xyz = max3_v3(x, y, z)
17	    result = max2(max_xyz, a10)
18	    return result
19
20	res = max10(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
def max5_v2(a, b, c, d,e):
    return max2(max2(max2(a,b),max2(c,d)),e)

return max2(max2(max2(a, b), max2(c, d)), e)
def max2(x,y):
    if x > y:
        return x
    else:
        return y   #a_1, a_2, a_3, a_4, a_5
# delete pass and fill in your code below
    if a_1 > a_2 and a_1 > a_3 and a_1 > a_4 and a_1 > a_5:
        return a_1
    elif a_2 > a_1 and a_2 > a_3 and a_2 > a_4 and a_2 > a_5:
        return a_2
    elif a_3 > a_1 and a_3 > a_2 and a_3 > a_4 and a_3 > a_5:
        return a_3
    elif a_4 > a_1 and d > a_2 and a_4 > a_3 and d > a_5:
        return a_4
    else:
        return a_5

def max3(a, b, c):
    return max2(a, max2(b, c))


def max5_v3(a_1, a_2, a_3, a_4, a_5):
    return max2(max2(max3(a_1,a_2,a_3),a_4),a_5)


 def max3(a, b, c):
     if a >= b and a >= c:
         return a
     elif b >= a and b >= c:
         return b
     else:
         return c


 def max2(a, b):
     if a > b:
         return a
     else:
         return b


 def max8(a, b, c, d, e, f, g, h):
     print(max3(max2(g, h), max3(d, e, f), max3(a, b, c)))

 #another example


 def func1(lst):
     for x in lst:
         amount = 0
         for y in lst:
             if x == y:
                 amount = amount + 1
         if amount >= 2:
             return True
     return False


 def func2(lst):
     amount = 0
     for x in lst:
         for y in lst:
             if x == y:
                 amount = amount + 1
         if amount >= 2:
             return True
     return False


 def func3(lst):
     for x in lst:
         if x in lst:
             return True
     return False


 def func4(lst):
     for x in lst:
         if lst.count(x) >= 2:
             return True
     return False


 def main():
     print(func1([1, 2, 3, 4]))


 main()

# Sample Input
# code sleep eat repeat
#
# Sample Output
# #codesleepeatrepeat
 s = input()


 def hashtagGen(text):
     ns = s.replace(" ", "")
     return ("#" + ns)
 print(hashtagGen(s))