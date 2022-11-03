# When squirrels get together for a party, they like to have cigars.
# A squirrel party is successful when the number of cigars is between 40 and 60,
# inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars.
# Return True if the party with the given values is successful, or False otherwise.

def cigar_party(cigars, is_weekend):
  if is_weekend:
    if cigars>=40:
      return True
    return False
  else:
    if cigars>=40 and cigars<=60:
      return True
    return False

#  You and your date are trying to get a table at a restaurant.
# The parameter "you" is the stylishness of your clothes, in the range 0..10,
# and "date" is the stylishness of your date's clothes. The result getting the' \
# ' table is encoded as an int value with 0=no, 1=maybe, 2=yes. ' \
# 'If either of you is very stylish, 8 or more, then the result is 2 (yes).' \
# ' With the exception that if either of you has style of 2 or less, then the result is 0 (no' \
# ' ). Otherwise the result is 1 (maybe).

def date_fashion(you, date):
  if you<=2 or date<=2:
    return 0
  if you>=8 or date>=8:
    return 2
  return 1


# The squirrels in Palo Alto spend most of the day playing. In particular, they play
# if the temperature is between 60 and 90 (inclusive). Unless it is summer, then the
# upper limit is 100 instead of 90. Given an int temperature and a boolean is_summer,
# return True if the squirrels play and False otherwise.


# squirrel_play(70, False) → True
# squirrel_play(95, False) → False
# squirrel_play(95, True) → True
def squirrel_play(temp, is_summer):
  if is_summer:
    if temp<=100 and temp>=60:
      return True
    return False
  if temp<=90 and temp>=60:
    return True
  return False


# You are driving a little too fast, and
# a police officer stops you. Write code
# to compute the result, encoded as an int value
# : 0=no ticket, 1=small ticket, 2=big ticket. If
# speed is 60 or less, the result is 0. If speed is
# between 61 and 80 inclusive, the result is 1. If speed is
# 81 or more, the result is 2. Unless it is your birthday --
# on that day, your speed can be 5 higher in all cases.
# caught_speeding(60, False) → 0
# caught_speeding(65, False) → 1
# caught_speeding(65, True) → 0
def caught_speeding(speed, is_birthday):
  if is_birthday:
    if speed<66:
      return 0
    elif  speed<=85 and speed>=66:
      return 1
    else:
      return 2
  else:
    if speed<61:
      return 0
    elif  speed<=80 and speed>=61:
      return 1
    else:
      return 2

# Given 2 ints, a and b, return their sum.
# However, sums in the range 10..19 inclusive,
# are forbidden, so in that case just return 20.
# sorta_sum(3, 4) → 7
# sorta_sum(9, 4) → 20
# sorta_sum(10, 11) → 21
def sorta_sum(a, b):
  sum=a+b
  if sum<=19 and sum>=10:
    return 20
  else:
    return sum

# 'Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat,'
# ' and a boolean indicating if we are on vacation, return a string of the '
# 'form "7:00" indicating when the alarm clock should ring. Weekdays, the alarm' \
# ' should be "7:00" and on the weekend it should be "10:00". Unless we are on vacation' \
# ' -- then on weekdays it should be "10:00" and weekends it should be "off".

def alarm_clock(day, vacation):
  if vacation:
    if day>=1 and day<=5:
      return "10:00"
    else:
      return "off"
  if day>=1 and day<=5:
      return "7:00"
  else:
    return "10:00"



# The number 6 is a truly great number. Given two int values, a and b,
# return True if either one is 6. Or if their sum or difference is 6.
# Note: the function abs(num) computes the absolute value of a number.
# love6(6, 4) → True
# love6(4, 5) → False
# love6(1, 5) → True


def love6(a,b):
  if a==6 or b==6 or a+b==6 or abs(a-b)== 6:
    return True
  return False


# 'Given a number n, return True if n is in the range' \
# ' 1..10, inclusive. Unless outside_mode is True, in which' \
# ' case return True if the number is less or equal to 1, or greater or equal to 10.
def in1to10(n, outside_mode):
  if outside_mode:
    if n<=1 or n>=10:
      return True
    return False
  if n>=1 and n<=10:
    return True
  return False


Given a non-negative number "num", return True if num is within 2 of a multiple of 10.
Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2.

def near_ten(num):
  if num%10==1 or num%10==2 or num%10==8 or num%10==9 or num%10==0:
    return True
  return False

Given 3 int values, a b c, return their sum. However, if one of the values
is the same as another of the values, it does not count towards the sum.

def lone_sum(a, b, c):
  if a==b and b==c:
    return 0
  if a==b:
    return c
  if a==c:
    return b
  if b==c:
    return a
  return a+b+c

# Given 3 int values, a b c, return their sum. However,
# if one of the values is 13 then it does not count towards the sum
# and values to its right do not count. So for example, if b is 13,
# then both b and c do not count.
def lucky_sum(a, b, c):
  if a==13:
    return 0
  if b==13:
    return a
  if c==13:
    return a+b
  return a+b+c

# Given 3 int values, a b c, return their sum. However, if any of the values
# is a teen -- in the range 13..19 inclusive -- then that value counts as 0, except
# 15 and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that takes
# in an int value and returns that value fixed for the teen rule. In this way, you avoid repeating
# the teen code 3 times (i.e. "decomposition"). Define the helper below and at the same indent level as the main no_teen_sum().
def no_teen_sum(a, b, c):
  a=fix_teen(a)
  b=fix_teen(b)
  c=fix_teen(c)
  return a+b+c

def fix_teen(n):
  if n==13 or n==14 or n==17 or n==18 or n==19:
    return 0
  return n

#
# For this problem, we'll round an int value up to the next multiple of 10' \
# ' if its rightmost digit is 5 or more, so 15 rounds up to 20. ' \
# 'Alternately, round down to the previous multiple of 10 if its rightmost' \
# ' digit is less than 5, so 12 rounds down to 10. Given 3 ints, a b c, return ' \
# 'the sum of their rounded values. To avoid code repetition, write a separate helper "def' \
#  " and call it 3 times. Write the helper entirely below ' \
#  'and at the same indent level as round_sum().

def round_sum(a, b, c):
  return round(a) + round(b) + round(c)


def round(n):
  last_dig = n % 10
  if last_dig >= 5:
    return 10 - last_dig + n
  if last_dig < 5:
    return n - last_dig

# We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23.
# We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.
# parrot_trouble(True, 6) → True
# parrot_trouble(True, 7) → False
# parrot_trouble(False, 6) → False
def parrot_trouble(talking, hour):
  return (talking and (hour < 7 or hour > 20))


# Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
# makes10(9, 10) → True
# makes10(9, 9) → False
# makes10(1, 9) → True
def makes10(a, b):
  return (a == 10 or b == 10 or a+b == 10)

# Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.
# near_hundred(93) → True
# near_hundred(90) → True
# near_hundred(89) → False
def near_hundred(n):
  return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))
