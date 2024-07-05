def find_length_of_string(str):
    i = 0
    while True:
        try:
            if str[i]:
                i += 1
        except IndexError:
            break
    print('length of  ', str, ' is ', i)


find_length_of_string('123456')
find_length_of_string('1234567')
find_length_of_string('12345678')
find_length_of_string('swap')
find_length_of_string('swapnil ingle')
