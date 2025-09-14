## calculate area of a rectangle
length = float(input("enter the length of the rectangle: "))
width = float(input("enter the width of the rectangle: "))

area = length * width

print("the area of the rectangle is:", area)

## take age and name to print a greeting
x = input("Enter your name: ")
y = input("enter your age: ") 

print("hello " + x, "your age is", y) 

## check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

number = int(input("enter a number: "))
result = check_even_odd(number)
print(f"the number {number} is {result}")

## find maximum and minimum values
numbers = [28, 28, 89, 346, 24, 58, 12, 900, 56, 42, 10, 95, 73]

smallest = largest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num

print(f"the smallest number is: {smallest}")
print(f"the largest number is: {largest}")

## check if palindrome
string_to_check = input('enter a string: ')

if string_to_check == string_to_check[::-1]:
    print('this is a palindrome')
else:
    print('this is not a palindrome')

##calculate compounded intrest
def compound_interest(principal, rate, time):

    Amount = principal * (pow((1 + rate / 100), time))
    CI = Amount - principal
    print("Compound interest is", CI)

principal = int(input("enter the principal amount: "))
rate = int(input("enter rate of interest: "))
time = int(input("enter the time in years: " ))

compound_interest(principal,rate,time)

## convert number of days into years/weeks/days
print(end="enter the number of days: ")
num = int(input())

year = int(num/365)
week = int((num%365)/7)
days = int((num%365)%7)

print("\nyear(s): "+str(year)+", week(s): "+str(week)+", day(s): "+str(days))

##find sum of positive numbers
a = (1, 48, 38, 95, 82, 56, 9, 2, 77)
x = sum(a) 
print(x)

##count the number of words in a given sentence
sentence = input("enter a sentence: ")
words_list = sentence.split()
number_of_words = len(words_list)
print("the sentence has ",number_of_words," word(s) in it")

##swap the value of two variables
x, y = 10, 50

x, y = y, x  

print("x:", x)
print("y:", y)