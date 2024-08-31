# 5. Default Parameter Value
# Problem: Write a function that greets a user. If no name is provided, it should greet with a default name.

def greet(name="Guest"):
  print("Hello, " + name + "!")

greet()  # Output: Hello, Guest!
greet("Alice")  # Output: Hello, Alice!
greet("Bob")  # Output: Hello, Bob!
greet("Charlie")  # Output: Hello, Charlie!