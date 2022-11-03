def binary_search(my_list, x):
    left = 0
    right = len(my_list)-1

    while left<=right:
        mid = (left+right)//2
        #print(mid, my_list[mid])
        if my_list[mid]==x:
            return True
        else:
            if my_list[mid] < x:    #go to right half
                left = mid+1
            else:                   #go to left half
                right = mid-1


def binary_search(L, x):
    left = 0
    right = len(L) - 1
    while left <= right:
        mid = (left + right) // 2
        if x == L[mid]:
            return True
        else:
            if x < L[mid]:  # go to left half
                right = mid - 1
            else:  # go to right half
                left = mid + 1
    return False  # if we got here the search failed


lst = [3, 4, 5, 6, 9, 10, 13, 16, 18, 20, 22, 28, 29, 31, 32, 33, 40, 42, 47, 48, 50, 52]
result = binary_search(lst, 17)
print(result)


lst = [1,7,6,3,4]
lst.remove(7)
print(lst)

lst = [1,7,6,3,4]
lst.append(lst[2])
print(lst)
lst.remove(min(lst))
print(lst)

def is_sorted(lst):
    for i in range (len(lst)-2):
        if lst[i] >lst[i+1]:
            return False
        else:
            return True

def selection_sort(L):
    n = len(L)
    sorted_L = []
    for i in range(n):
        minimum = min(L)
        L.remove(minimum)
        sorted_L.append(minimum)
    return sorted_L


def selection_sort2(L):
# Write your solution here!
# n=len(L)
# sorted_L=[]
# for i in range(n):
#     maximum=max(L)
#     L.remove(maximum)
#     sorted_L.append(maximum)
# return sorted_L


import random
import time


def generate_random_list(n):
    ''' returns a list of size n with random integers between 0 and 999999
        Uses random.randint(a,b) which randomly picks an integer between a and b
    '''
    return [random.randint(0, 999999) for i in range(n)]  # a short way to generate the list


def selection_sort(L):
    ''' return a sorted copy of L '''
    n = len(L)
    sorted_L = []
    for i in range(n):
        minimum = min(L)
        L.remove(minimum)
        sorted_L.append(minimum)
    return sorted_L


for n in [1000, 2000, 4000]:
    lst = generate_random_list(n)

    start = time.clock()
    lst2 = selection_sort(lst)  # lst2 not used
    end = time.clock()

    print("Number of elements in the list: ", n)
    print("Time measured for selection_sort: ", end - start, " seconds")/
    print()  # just a new line




# def search_print(L, x):
#     for e in L:
#         if e == x:
#             return e
#     # if we got here the search failed
#     return False
#
# print(search_print)
# ### TESTS ###
#
# # so we can tell you what the correct printouts should be
#
# L = [4, 7, 2, 3, 1]  # an input list
#
# print("********************")
# print("Starting the test:")
#
# for x in [7, 8]:
#     print("*******************")
#     print("L =", L, ", x =", x)
#     print("--------------------")
#     print("Your printouts:")
#     search_print(L, x)
#     print("--------------------")
#     print("The correct printouts:")
#     sol.search_print(L, x)
#
# print("********************")
# print("Tests concluded, add more tests of your own below!")
# print("********************")

def selection_sort(L):
    n = len(L)
    sorted_L = []
    for i in range(n):
        minimum = min(L)
        L.remove(minimum)
        sorted_L.append(minimum)

    return sorted_L


L = [1, 4, 5, 2, 3]
result = selection_sort(L)
print(result)



