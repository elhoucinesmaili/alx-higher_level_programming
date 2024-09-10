import random

# Generate a random integer between -10000 and 10000
number = random.randint(-10000, 10000)

# Determine the last digit (handling negative numbers)
if number < 0:
    last_digit = number % -10
else:
    last_digit = number % 10

# Print the base message
print(f"Last digit of {number} is {last_digit}", end=" ")

# Determine the additional message based on the value of the last digit
if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
