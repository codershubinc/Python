# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).


password = '1234uidl78Thu5'
length = len(password)

if length < 6:
    print('Weak')
elif length < 10:
    print('Medium')
else:
    print('Strong')