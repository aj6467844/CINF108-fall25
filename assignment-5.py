def sum_of_positives(numbers):
    return sum(num for num in numbers if num > 0)

# Example usage:
numbers = [1, -2, 3, 4, -5, 6]
print(sum_of_positives(numbers))  

## return factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage:
number = int(input("Enter a number: "))
print("Factorial is", factorial(number))

##find the square of each element
def sum_of_positives(numbers):
    return sum(num for num in numbers if num > 0)

numbers = [1, -2, 3, 4, -5, 6]
print(sum_of_positives(numbers))

def factorial(n):
    return 1 if n in (0, 1) else n * factorial(n - 1)

number = int(input("Enter a number: "))
print("Factorial is", factorial(number))

def squares(lst):
    return [x**2 for x in lst]

nums = [1, 2, 3, 4, 5]
print("Squares:", squares(nums))

##check if even or odd
def check_even_odd(n):
    return "even" if n % 2 == 0 else "odd"

# Example usage:
num = int(input("Enter a number: "))
print(check_even_odd(num))

##area of triangle
def area_of_triangle(base, height):
    return 0.5 * base * height

# Example usage:
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
print("Area of the triangle is", area_of_triangle(base, height))

##list intersection
def list_intersection(list1, list2):
    return [item for item in list1 if item in list2]

# Example usage:
a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]
print("Intersection:", list_intersection(a, b))

##leap year
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# Example usage:
year = int(input("Enter a year: "))
print("Leap year" if is_leap_year(year) else "Not a leap year")

##multiplication
def print_multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

# Example usage:
num = int(input("Enter a number to print its multiplication table: "))
print_multiplication_table(num)

##menu
def sum_of_positives(numbers):
    return sum(num for num in numbers if num > 0)

def factorial(n):
    return 1 if n in (0, 1) else n * factorial(n - 1)

def squares(lst):
    return [x**2 for x in lst]

def check_even_odd(n):
    return "even" if n % 2 == 0 else "odd"

def area_of_triangle(base, height):
    return 0.5 * base * height

def list_intersection(list1, list2):
    return [item for item in list1 if item in list2]

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def print_multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

def main():
    while True:
        print("\nMenu:")
        print("1. Sum of positive numbers in a list")
        print("2. Factorial of a number")
        print("3. Square of each element in a list")
        print("4. Check if a number is even or odd")
        print("5. Area of a triangle")
        print("6. Intersection of two lists")
        print("7. Check if a year is a leap year")
        print("8. Print multiplication table")
        print("9. Exit")
        choice = input("Enter your choice (1-9): ")

        if choice == "1":
            numbers = list(map(int, input("Enter numbers separated by space: ").split()))
            print("Sum of positives:", sum_of_positives(numbers))
        elif choice == "2":
            number = int(input("Enter a number: "))
            print("Factorial is", factorial(number))
        elif choice == "3":
            nums = list(map(int, input("Enter numbers separated by space: ").split()))
            print("Squares:", squares(nums))
        elif choice == "4":
            num = int(input("Enter a number: "))
            print(check_even_odd(num))
        elif choice == "5":
            base = float(input("Enter the base of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            print("Area of the triangle is", area_of_triangle(base, height))
        elif choice == "6":
            list1 = list(map(int, input("Enter first list (space separated): ").split()))
            list2 = list(map(int, input("Enter second list (space separated): ").split()))
            print("Intersection:", list_intersection(list1, list2))
        elif choice == "7":
            year = int(input("Enter a year: "))
            print("Leap year" if is_leap_year(year) else "Not a leap year")
        elif choice == "8":
            num = int(input("Enter a number to print its multiplication table: "))
            print_multiplication_table(num)
        elif choice == "9":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()