# 9. Generator Function with yield
# Problem: Write a generator function that yields even numbers up to a specified limit.

def even_numbers_generator(limit):
    for i in range(1, limit+1):
        if i % 2 == 0:
            yield i


limit = 10
even_numbers = even_numbers_generator(limit)

for number in even_numbers:
    print(number)