# 7. Function with *args
# Problem: Write a function that takes variable number of arguments and returns their sum.

def sum(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


print(sum(3, 5))
print(sum(5, 7))
print(sum(9, 11, 5, 5, 5, 723, 5475, 545, 87, 53, 346546, 54654,756, 547457, 56756, 67567, 56756, 756756, 756, 546))
