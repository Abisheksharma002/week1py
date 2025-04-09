#a) Implement Python Script to generate first N natural numbers
def generate_natural_numbers(n):
    return list(range(1, n + 1))

n = int(input("Enter the value of N: "))
print("First N natural numbers:", generate_natural_numbers(n))

#b) Implement Python Script to check given number is palindrome or not.
def is_palindrome(number):
    str_num = str(number)
    return str_num == str_num[::-1]

num = int(input("Enter a number: "))
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")

#c) Implement Python script to print factorial of a number.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}")

#d) Implement Python Script to print sum of N natural numbers.
def sum_of_natural_numbers(n):
    return n * (n + 1) // 2

n = int(input("Enter the value of N: "))
print(f"Sum of first {n} natural numbers is {sum_of_natural_numbers(n)}")

#e) Implement Python Script to check given number is Armstrong or not.
def is_armstrong(number):
    digits = [int(digit) for digit in str(number)]
    return number == sum([digit ** len(digits) for digit in digits])

num = int(input("Enter a number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

#f) Implement Python Script to generate prime numbers series up to n
def generate_primes(n):
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

n = int(input("Enter the value of N: "))
print(f"Prime numbers up to {n}:", generate_primes(n))
