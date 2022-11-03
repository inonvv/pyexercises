from math import acos, degrees


def calcalteTriangle(x,y,z):
    angle=degrees(acos((x**2+y**2-z**2)/(x*y*2)))
    if x==y==z:
        return "equilateral triangle"
    elif x==y or x==z or y==z:
        return "isosceles triangle"
    elif angle>90:
        return "obtuse triangle"
    elif angle<90:
        return "sharp angle"
    elif angle==90:
        return "right-angle triangle"


def main():
    x=float(input("x-"))
    y=float(input("y-"))
    z=float(input("z-"))
    print(calcalteTriangle(x,y,z))

main()