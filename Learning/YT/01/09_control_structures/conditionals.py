# conditionals
is_true = True

# if

if is_true:
    print('True')

# if else

if is_true:
    print('True')
else:
    print('False')

# if elif else

fruit = 'mango'
if fruit == 'apple':
    print('this is ', fruit)
elif fruit == 'banana':
    print('this is ', fruit)
else:
    print('Unknown fruit')

# ternary operator
identify_fruit = 'apple' if fruit == 'apple' else fruit + ' is new fruit'
print(identify_fruit)


# nested if

if is_true:
    if fruit == 'apple':
        print('this is ', fruit)
    elif fruit == 'banana':
        print('this is ', fruit)
    else:
        print('Unknown fruit')



# nested if else
if is_true:
    if fruit == 'apple':
        print('this is ', fruit)
    elif fruit == 'banana':
        print('this is ', fruit)
    else:
        print('Unknown fruit')
else:
    print('False')

# nested ternary operator

if is_true:
    identify_fruit = 'apple' if fruit == 'apple' else fruit + ' is new fruit'
    print(identify_fruit)
else:
    print('False')

# short circuiting

if is_true and fruit == 'apple':
    print('this is ', fruit)
elif fruit == 'banana':
    print('this is ', fruit)
else:
    print('Unknown fruit')

# logical operators

if is_true==False and fruit == 'apple' and 1>0:
    print('this is ', fruit)
elif fruit == 'banana' or fruit == 'mango':
    print('this is ', fruit)
else:
    print(fruit + " is now known fruit")




