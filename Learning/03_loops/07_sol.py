# Problem: Keep asking the user for input until they enter a number between 1 and 10.


while True:
    number = int(input("Enter a number between 1 and 10: "))

    if number >= 1 and number <= 10:
        break
    else:
        print("Invalid input!")
print("Thank you!")