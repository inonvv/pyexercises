 for i in range(10):
        print(i)

    for i in range(10):
        print(i,end="")

    if n % 11 == 0:
        print("boom!")
for i in range(10,2,-2):
    print(i,end=","
    for i in range(10, 26, 1):
        print(i , end=",")
    if i % 5 == 0:
        print("awesome")
        # print string forward & backward
    def print_string():
    name = "Monty Python"
    print(name(
        print(name[::-1](
  def main():
        print_string)(
    main()
for i in range(len(nums)):
    sums = nums[i]
    if sums == target:
        return [i, i]
    for j in range(i + 1, len(nums)):
        sums = sums + nums[j]
        if sums == target:
            return [i, j]
        elif sums > target:
            break

    for grade in [90, 100, 85, 85, 75, 95]:
        print(grade)
        print(max([90, 100, 85, 85, 75, 95]))

    st = "abcdefg"
    for char in st:
        print(char)
    print('goodbye!')
#def mystery(string):
#     x = 0
#     for char in string:
#         if char == "!":
#              x = x + 1
#     return x
#
# print(mystery("Hello!! Wor ld!!"))
 #
 #
 # def my_max(lst):
 #     maximum = lst[0]
 #     for x in lst:
 #         if x > maximum:
 #             maximum = x
 #     return maximum
 #
 # def my_min(lst):
 #     minimum = lst[0]
 #     for x in lst:
 #         if x < minimum:
 #             minimum = x
 #     return minimum



 # #print(my_max([3,4,2,5,1]))
 # #L = [3,4,2,5,1]
 # L = ["orange", "egg", "banana","carrot","peach"]
 # print(my_min(L))
 #
 # def count_spaces(s):
 #     cnt = 0
 #     for char in s:
 #         if char == " ":
 #             cnt = cnt+1
 #     return cnt


 #def count_char(s, c):
     # delete pass and fill in your code below
     pass
def count_spaces(s):
    cnt = 0
    for char in s:
        if char == " ":
            cnt = cnt+1
    return cnt


def count_char(s, c):
    # delete pass and fill in your code below
    cnt = 0
    for char in s:
        if char == "c":
            cnt = cnt + 1
    return cnt

p = 1
for num in range(1,5):
    p = p * num
print(p)
def sum_range(start, end):
    s = 0
    for num in range(start, end+1):
        s = s+num
    return s

def sum_range2(start, end):
    return sum(range(start, end+1))


# Time comparison for summing over range
def sum_range(start, end):
    s = 0
    for num in range(start, end+1):
        s = s+num
    return s


def sum_range2(start, end):
    return sum(range(start, end+1))


# Time measurement
import time

start = time.clock()
res = sum_range(1, 10**8)
end = time.clock()

print('The sum of 1+2+...+10**8 is', res, 'and the time it took to compute it is', end-start, 'seconds')



# n = 10**8
# res = n*(n+1)//2
 # def num_arr_max(lst):
 #     maximum = lst[0]
 #     for x in lst:
 #         if x > maximum:
 #             maximum = x
 #     return maximum
 #
 #
 # def str_arr_max(lst):
 #     longest_word = lst[0]
 #     for s in lst:
 #         if len(s) > len(longest_word):
 #             longest_word = s
 #     return longest_word[0]

def between(lst, a, b):
    count=0
    for x in lst:
        if x>a and x<b:
            count+=1
    return count

def avg(L):
    s = 0
    for num in L:
        s = s + num
    return s / len(L)


def is_positive_int(st):
    result=True
    firstTime=True
    for x in st:
        if firstTime==True:
            if x<"1" or x>"9":
                result=False
            firstTime=False
        else:
            if x<"0" or x>"9":
                result=False
    return result

print(is_positive_int(" ")


def sum_range(start, end):
    s = 0
    for num in range(start, end+1):
        s = s + num
    return s

def sum_range2(start, end):
    s = 0
    num = start
    while num <= end:
        s = s+ num
        num = num + 1
    return s

def avg(L):
    s = 0
    i = 0
    while i < len(L) :
         s = s + L[i]
         i=i+1
    return s/len(L)




def albert(dig1,dig2,dig3):
    absoluteNum=(dig1*100)+(dig2*10)+dig3
    reverse= int(str(absoluteNum)[::-1])
    finalNum=absoluteNum-reverse
    if dig1<0 and dig2<0 and dig3<0:
        return "this are invalid number please try again"
    elif dig1==dig3:
        return "the first and the last digits should be different"
    elif finalNum<0:
        return "try again"
    elif absoluteNum>reverse:
        return finalNum
    elif reverse>absoluteNum:
        return finalNum


def main():
    digit1= int(input("digit1"))
    digit2= int(input("digit2"))
    digit3= int(input("digit3"))
    print(albert(digit1,digit2,digit3))

main()


a =int(input())
b =int(input())
numbers = list(range(a,b))
print(numbers)