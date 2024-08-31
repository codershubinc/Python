# find length of string with  loop

str = 'cust string for test of cust length method'
i = 0

while True:
    try:
        if str[i]:
            i += 1
    except IndexError:
        break

print('Length of string is ', i)
print('Length of string by in build method is ', len(str))
