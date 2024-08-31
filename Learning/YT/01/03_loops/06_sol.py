# Problem: Compute the factorial of a number using a while loop.


number = 5
factorial = 1
i = 1
while i <= number:
    factorial *= i
    i += 1

print( number, "factorial = ", factorial)