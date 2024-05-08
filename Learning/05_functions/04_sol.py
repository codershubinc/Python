# 4. Function Returning Multiple Values
# Problem: Create a function that returns both the area and circumference of a circle given its radius.
# take precision upto 2 decimal places


import math


def area_and_circumference(radius):
    area = round((math.pi * radius**2), 2)
    circumference = round(2 * math.pi * radius, 2)
    return area, circumference


area, circumference = area_and_circumference(5)
print("Area: ", area)
print("Circumference: ", circumference)
