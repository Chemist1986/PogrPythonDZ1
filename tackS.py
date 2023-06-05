# 1

# def print_tree(height):
#     for i in range(1, height+1):
#         print(''*(height-i)+'*'*(2*i-1))
        
# print_tree(5)


# 2

# def multiplication_table(n):
#     for i in range(1, n + 1):
#         for j in range(1, n + 1):
#             print(f"{i} x {j} = {i * j}\t", end="")
#         print()

# # Example usage: display multiplication table up to 10
# multiplication_table(10)

# 3

# def classify_triangle(a, b, c):
#     if a + b <= c or a + c <= b or b + c <= a:
#         print("Triangle cannot be formed with the given side lengths.")
#     elif a == b and b == c:
#         print("Equilateral triangle.")
#     elif a == b or b == c or a == c:
#         print("Isosceles triangle.")
#     else:
#         print("Scalene triangle.")

# # Example usage:
# a = float(input("Enter the length of side a: "))
# b = float(input("Enter the length of side b: "))
# c = float(input("Enter the length of side c: "))

# classify_triangle(a, b, c)


# 4

# def is_prime(number):
#     if number < 2:
#         return False
#     for i in range(2, int(number**0.5) + 1):
#         if number % i == 0:
#             return False
#     return True

# # Get user input
# number = int(input("Enter a number: "))

# # Check if the number is prime or composite
# if number < 0 or number > 100000:
#     print("Number out of range.")
# else:
#     if is_prime(number):
#         print("Prime number.")
#     else:
#         print("Composite number.")


# 5

import random

def guess_number():
    target_number = random.randint(0, 1000)
    attempts = 10

    print("Guess the number between 0 and 1000!")
    while attempts > 0:
        guess = int(input("Enter your guess: "))
        if guess < target_number:
            print("Greater than")
        elif guess > target_number:
            print("Less than")
        else:
            print("Congratulations! You guessed the number correctly!")
            return
        attempts -= 1

    print("Game over! You ran out of attempts. The target number was:", target_number)

# Run the game
guess_number()