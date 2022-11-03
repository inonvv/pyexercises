# Given a string, return the count of the number of times that a substring
# length 2 appears in the string and also as the last 2 chars of the string,
# so "hixxxhi" yields 1 (we won't count the end substring).


# Given an array of ints, return True if one
# of the first 4
# elements in the array is a 9.
# The array length may be less than 4.
def array_count9(nums):
    count = 0
    for i in nums:
        if i == 9:
            count = count + 1
    return count



def array_front9(nums):
    num = 4
    if len(nums) < num:
        num = len(nums)
    for i in range(num):
        if nums[i] == 9:
            return True
    return False



# Given an array of ints, return True if the sequence of numbers 1, 2, 3
#appears in the array somewhere.

def array123(nums):
  for i in range (len(nums)-2):
    if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
      return True
  return False

#
# Given 2 strings, a and b, return the number of the positions where
# they contain the same length 2 substring. So "xxcaazz" and "xxbaaz"
# yields 3, since the "xx", "aa", and "az" substrings appear in the
# same place in both strings.

def string_match(a, b):
  counter=0
  short=len(a)
  if len(a)>len(b):
    short=len(b)
  for i in range (short-1):
    if a[i]==b[i] and a[i+1]==b[i+1]:
      counter=counter+1
  return counter


# Given an array of ints, return True if 6 appears as
# either the first or last element in the array. The array
# will be length 1 or more.

def first_last6(nums):
  if 6==nums[0] or 6==nums[len(nums)-1]:
    return True
  else:
    return False

def same_first_last(nums):
        for i in nums:
            if nums < 1:
                return False
            if nums[0] == nums[len(nums) - 1]:
                return True
        return False



def common_end(a, b):
  if a[0]==b[0] or a[len(a)-1]==b[len(b)-1]:
    return True
  else:
    return False

def sum3(nums):
  sum=0
  for i in nums:
    sum=sum+i
  return sum


def rotate_left3(nums):
    a=nums[0]
    b=nums[1]
    c=nums[len(nums)-1]
    nums[0]=b
    nums[1]=c
    nums[len(nums)-1]=a
    return nums


def reverse3(nums):
    newNums = []
    newNums = nums[::-1]
    return newNums


def max_end3(nums):
    max=nums[0]
    if max<nums[len(nums)-1]:
      max=nums[len(nums)-1]
    for i in range(len(nums)):
      nums[i]=max
    return nums

# Given an array of ints, return the sum of the first 2
# elements in the array. If the array length is less than 2,
# just sum up the elements that exist, returning 0 if the array is length 0.
def sum2(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    else:
        return nums[0] + nums[1]




#Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.


def middle_way(a, b):
  new=[]
  newA=a[1]
  newB=b[1]
  new.append(newA)
  new.append(newB)
  return new




Given an array of ints, return a
new array length 2 containi g the
first and last elements from the original array.
The original array will be length 1 or more


def make_ends(nums):
  new=[]
  first=nums[0]
  last=nums[len(nums)-1]
  new.append(first)
  new.append(last)
  return new



Given an int array length 2, return True if it contains a 2 or a 3.

if nums[0]==2 or nums[0]==3:
    return True
  if nums[1]==2 or nums[1]==3:
    return True
  return False