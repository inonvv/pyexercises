n = 0
while n < 10:
    print(n)
    n = n + 1
print(“goodbye”)



חיפוש סדרתי (קלט: רשימה L, ערך  X):

1. הגדר משתנה i=0
2. כל עוד i קטן מאורך הרשימה
2.1 אם האיבר באינדקס i של L (כלומר L[i] ) שווה ל- x:
2.1.1 החזר True (וסיים)
2.2 הגדל את i ב-1
3. (אם הגעת לכאן) החזר False
בשפת פייתון, הפקודה בשורה מספר 2 תתורגם כך:

while i<len(L):

# You have a magic box that doubles the count of items you put, in every day.
# The given program takes the initial count of the items and the number of days as input.
# Write a program to calculate and output items' count on the last day.
items = int(input())
days = int(input())
# your code goes here
while days > 0:
    items *= 2
    days -= 1
print(items)