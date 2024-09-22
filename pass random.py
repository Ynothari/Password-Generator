import random

def generate_password(n):
    password = ""
    for _ in range(n):
        password += str(random.randint(0, 9))
    return password

if __name__ == "__main__":
    try:
        n = int(input("How many digits in the password? "))
        if n <= 0:
            print("The number of digits should be a positive integer.")
        else:
            print(f"Generated password: {generate_password(n)}")
    except ValueError:
        print("Please enter a valid integer.")


