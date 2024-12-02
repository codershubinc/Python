a = 0
b =  self
# TODO : implement error handling

try:
    print(a+b)
except ZeroDivisionError as e :
    print("cannot divide by zero")
except ValueError as e:
    print("value error")
except TypeError as e:
    print("type error")
except:
    print("error")
finally:
    print("cleaning up")


 