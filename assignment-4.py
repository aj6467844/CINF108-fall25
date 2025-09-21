# Program to check if a year is a leap year

year = int(input("Enter a year: "))

if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# Find all even numbers in a list and store them in a new list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Example list
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print("Even numbers:", even_numbers)

# Program to check if a number is a prime number

num = int(input("Enter a number to check if it is prime: "))

if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

# Program to generate a Fibonacci sequence up to a given number of terms

n_terms = int(input("Enter the number of terms for the Fibonacci sequence: "))

fib_sequence = []

a, b = 0, 1
for _ in range(n_terms):
    fib_sequence.append(a)
    a, b = b, a + b

print("Fibonacci sequence:", fib_sequence)

# Program to print all names starting with the letter 'A' from a list

names = ["Alice", "Bob", "Angela", "Michael", "Andrew", "Sophie", "Alex"]  # Example list

print("Names starting with 'A':")
for name in names:
    if name.startswith('A'):
        print(name)

# Program to print the multiplication table of a given number

num = int(input("Enter a number to print its multiplication table: "))

print(f"Multiplication table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Program to calculate the factorial of a given number

num = int(input("Enter a number to calculate its factorial: "))

factorial = 1
if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}.")

# Program to print all prime numbers between 1 and 50

print("Prime numbers between 1 and 50:")
for num in range(2, 51):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)

# Program to count the number of words with more than five characters in a list

words = ["python", "code", "assignment", "list", "character", "hello", "world"]  # Example list

count = 0
for word in words:
    if len(word) > 5:
        count += 1

print(f"Number of words with more than five characters: {count}")

# Program to calculate the sum of digits of a given number

num = int(input("Enter a number to find the sum of its digits: "))

sum_digits = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum_digits += digit
    temp //= 10

print(f"The sum of the digits of {num} is {sum_digits}.")

