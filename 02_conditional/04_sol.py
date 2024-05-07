# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)


fruit = 'Banana'
color = 'Green'


if fruit == 'Banana':
    if color == 'Green':
        print('Unripe')
    elif color == 'Yellow':
        print('Ripe')
    else:
        print('Overripe')
else:
    print('Not a Known fruit')