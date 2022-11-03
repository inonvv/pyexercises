L = [1, 2, 1, 1, 3, 1, 2,1,1]
result = L.count(1)
print(result)
L = [1, 2, 3]
L.append(4)
print(L)
L = ["Hello", "Shalom", "Marhaba"]
L.append("Bonjour") #add element at the end of list
print(L)
L.remove("Hello") #remove element from list
print(L)
L = L * 2
print(L)
L.insert(2, "Hola") #insert "Hola" at index 2, push forward the elements after it
print(L)
print(L.count("Hello"))
L.reverse() #method reverse has no parameters
print(L)
print("Thank you!")

 # String find operations
st = "I am a string"
print(st.find("m"))
print(st.find("s"))
print(st.find("a"))
print(st.find(" "))
print(st.find("x"))
st = "I am a string"
print(st.replace("a", "A")) #replace every "a" by "A"
print(st.replace(" ", "_"))   #replace every space by "_"
print(st)  #did st

st = st.replace("a", "A")
import random
# Given a string, return a new string where "not " has been added to the front. However,
# if the string already begins with "not", return the string unchanged.
#
#
# not_string('candy') → 'not candy'
# not_string('x') → 'not x'
# # not_string('not bad') → 'not bad


def not_string(str):
    newStr = "not"
    if newStr == str.split(' ', 1)[0]:
        return str

    else:
        return "not " + str





def mult_and_replace(string):
    str=int(string.count('!'))
    newStr=""
    replacedstr=""
    for i in range(str):
        newStr = newStr+string
    replacedstr = newStr.replace('!','?')
    return replacedstr

print(mult_and_replace("hello!!"))


def print_string(name):
    name=name.replace(name[0],name[0].upper(),1)
    print(name)
    #print(name.upper())

def main():
    print_string("inon vinogradsky  ")

main()


def what (a, b):
    res = a
    for i in range(b):
        res = res + 1
    return res
print(what(5,7)


def what(a, b):
    i = 0
    res = a
    while i < b:
        res = res + 1
        i = i + 1
    return res


#def missing_char(str, n):
   # if len(str)>n:
     # str=str[0 : n : ] + str[n + 1 : :]
   # return str

def missing_char(str, n):
  front = str[:n]   # up to but not including n
  back = str[n+1:]  # n+1 through end of string
  return front + back


def front_back(str):
    if len(str) == 0:
        return str

    newStr = 0
    first = str[0]
    last = str[len(str) - 1]
    newStr = str.replace(last, first)
    newStr = newStr.replace(first, last, 1)
    return newStr


def front_back(str):
    if len(str) <= 1:
        return str

    mid = str[1:len(str) - 1]  # can be written as str[1:-1]

    # last + mid + first
    return str[len(str) - 1] + mid + str[0]

# Given a string, we'll say that the front is the first 3 chars of the string.' \
#  ' If the string length is less than 3, the front is whatever is there.' \
#  ' Return a new string which is 3 copies of the front.

def front3(str):
    str3 = ""
    if len(str) < 3:
        str3 = str
    else:
        str3 = str[:3]
    str3 = str3 * 3
    return str3

def front3(str):
  # Figure the end of the front
  front_end = 3
  if len(str) < front_end:
    front_end = len(str)
  front = str[:front_end]
  return front + front + front





# Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars,' \
#  or whatever is there if the string is less than length 3. ' \
# 'Return n copies of the front;
def front_times(str, n):
    front_end = 3
    if len(str) < front_end:
        front_end = len(str)
    strn = str[:front_end] * n
    return strn

# Given a string, return a new string made of every other char starting
# with the first, so "Hello" yields "Hlo".
def string_bits(str):
    newStr = ""
    for i in range(len(str)):
        if i % 2 == 0:
            newStr = newStr + str[i]
    return newStr



#Given a non-empty string like "Code" return a string like "CCoCodCode".

def string_splosion(str):
  newStr=""
  for i in range (len(str)+1):
    newStr=newStr+str[:i]
  return newStr



#Given a string, return the count of the number of times that a substring
# length 2 appears in the string and also as
#the last 2 chars of the string, so "hixxxhi" yields 1
#   (we won't count the end substring).
def last2(str):
  endOf=str[len(str)-2:]
  count=0
  for i in range (len(str)-2):
    if str[i]+str[i+1]==endOf:
      count=count+1
  return count


שרשור מחזרוזות
def hello_name(name):
  return "Hello "+ name+"!"

def make_tags(tag, word):
  stag="<"+tag+">"
  etag="</"+tag+">"
  return stag + word +etag

# Given an "out" string length 4, such as "<<>>",
# and a word, return a new string where the word is
# n the middle of the out string, e.g. "<<word>>".

def make_out_word(out, word):
  half1=out[:len(out)/2]
  half2=out[len(out)/2:]
  return half1 + word + half2



# Given a string, return a new string made of 3 copies of the
# last 2 chars of the original string. The string length will
# be at least 2.

def extra_end(str):
    newStr = str[len(str) - 2:]
    return newStr * 3


# Given a string, return the string made of its first two chars,
# so the String "Hello" yields "He". If the string is shorter than
# length 2, return whatever there is, so "X" yields "X", and the empty
# string "" yields the empty string "".

def first_two(str):
    short = 2
    if len(str) < short:
        short = len(str)
    newStr = str[:short]
    return newStr

# Given a string of even length, return the first half.
# So the string "WooHoo" yields "Woo".

def first_half(str):
  newStr=str[:len(str)/2]
  return newStr


# Given a string, return a version without the first and last char, so
# "Hello" yields "ell".
# The string length will be at least 2.
def without_end(str):
  newSTR=str[1:len(str)-1]
  return newSTR

# Given 2 strings, a and b, return a string of the form short+long+short,
# with the shorter string on the outside and the longer string on the inside.
# The strings will not be the same length, but they may be empty (length 0).
def combo_string(a, b):
    if len(a) > len(b):
        return b + a + b
    else:
        return a + b + a

# Given a string, return a "rotated left 2"
# version where the first 2 chars are moved
# to the end. The string length will be at least 2.

def left2(str):
  a=str[:2]
  b=str[2:]
  return b+a

