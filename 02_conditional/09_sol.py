# Problem: Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).


year = 2010

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(year, 'is a leap year')
else:
    print(year, 'is not a leap year')