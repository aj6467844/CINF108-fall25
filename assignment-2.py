## given a list of numbers find the sum and average
a = [5, 10, 15, 25, 40, 65, 100, 150]

total = sum(a)
avg = total / len(a)

print('sum      = ', total)
print('average  = ', avg)

## create a program that takes a temperature in celcius and converts it to kelvin
celTemp = input("enter temperature in celcius: ")
 
kelTemp = float(celTemp) + 273.15
 
print(str(celTemp) + ' degrees celsius is ' + 
      str(kelTemp) + ' kelvin.')

## implement a program that checks if a given string is a palendrome
string_to_check = input('enter a string: ')

if string_to_check == string_to_check[::-1]:
    print('this is a palindrome')
else:
    print('this is not a palindrome')

## creaste a funtion to reverse a given string
def reverse_string(input_string):
    return input_string[::-1]

string = input('type something to reverse: ')
reversed_string = reverse_string(string)
print('reversed: ',reversed_string)

## given a list of names concatenate them into a single string separated by spaces
names = ['willoughby', 'janie', 'holly', 'ethel']

result = " ".join(names)
print(result)

## check if given string is a pangram
import string

def is_pangram(s):
    return set(string.ascii_lowercase) <= set(s.lower())

print(is_pangram('the quick brown fox jumps over a lazy dog'))

## calculate the area and circumference of a circle given its radius
import math

def calculate_area(radius):
    area = math.pi * radius ** 2
    return area

def calculate_circumference(radius):
    circumference = 2 * math.pi * radius
    return circumference

radius = float(input("enter the radius of the circle: "))

area = calculate_area(radius)
circumference = calculate_circumference(radius)

print(f"the area is: {area}")
print(f"the circumference is: {circumference}")

## convert minnutes to hours and minutes
total_minutes = int(input("enter minutes: "))
hours = total_minutes // 60
minutes = total_minutes % 60

print(f"{total_minutes} minutes = {hours} hours and {minutes} minutes")

## create a function to count the number of vowels in a given string
def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0  
    
    for char in input_string:
        if char in vowels:
            count += 1
    return count

text = input("type for vowls: ")
print(f'the number of vowels is: {count_vowels(text)}')

## check if a number is prime
number = int(input("enter the number: "))

flag = False

for i in range (2, number):
    if(number % i == 0):
       flag = True
       break

if flag:
    print("the number {} is not prime".format(number))
else:
    print("the number {} is prime".format(number))