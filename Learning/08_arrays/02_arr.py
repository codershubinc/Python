arr = [
    'india',
    'australia',
    'usa',
    'uk',
    'canada',
    'france',
    'japan',
    'germany',
    'switzerland',
    'russia',
]

print(arr)

#  map takes two arguments first is function and second is iterable
#  this is map function with len function
map_the_arr = map(len, arr)

# here list function is used to convert map object to list
print(list(map_the_arr))

#  this is map function with str function
#  str function is used to convert int to string
map_the_arr = map(str, arr)

print(list(map_the_arr))

#  this is map function with upper case function
#  upper case function is used to convert string to upper case
map_the_arr = map(str.upper, arr)

print(list(map_the_arr))

#  this is map function with lower case function
#  lower case function is used to convert string to lower case
map_the_arr = map(str.lower, arr)

print(list(map_the_arr))

#  this is map function with title case function
#  title case function is used to convert string to title case first letter to capital
map_the_arr = map(str.title, arr)

print(list(map_the_arr))

#   this is map function with capitalize function
#   capitalize function is used to convert string to capitalize
map_the_arr = map(str.capitalize, arr)

print(list(map_the_arr))

