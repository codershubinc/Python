# Problem: Check if a number is prime.


number = 77
is_prime = True
for i in range(2, number):
    if number % i == 0:
        is_prime = False
        break

print( number, "prime = ", is_prime)