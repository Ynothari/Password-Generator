import random

# Get the number of digits for the password
n = int(input("How many digits? "))

# Generate and print the digits
for i in range(n):
    digit = random.randint(0, 9)
    print(digit, end=" ")

