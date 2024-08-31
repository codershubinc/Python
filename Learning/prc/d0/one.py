print('test')


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    



print("factorial of 5 is a " , factorial(5))
print("factorial of 6 is a " , factorial(6)) 