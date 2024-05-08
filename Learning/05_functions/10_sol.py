# 10. Recursive Function
# Problem: Create a recursive function to calculate the factorial of a number.

def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)

print(factorial(5))


    # """
    # Calculates the factorial of a given number using recursion.

    # Parameters:
    #     number (int): The number for which the factorial needs to be calculated.

    # Returns:
    #     int: The factorial of the given number.
    # """