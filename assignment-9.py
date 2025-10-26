import csv
import json
import math
import os

# 1. Student Class
class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def display_info(self):
        print(f"\nStudent Name: {self.name}, Age: {self.age}, Grades: {self.grades}")


# 2. Employee Class (uses CSV file)
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = float(salary)

    def display_info(self):
        print(f"Name: {self.name}, Position: {self.position}, Salary: ${self.salary:,.2f}")


def load_employees_from_csv(filename="employees2.csv"):
    if not os.path.exists(filename):
        print(f"File '{filename}' not found. Please create it first.")
        return
    with open(filename, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            e = Employee(row['name'], row['position'], row['salary'])
            e.display_info()


# 3. BankAccount Class
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")
        else:
            print("Insufficient funds!")


# 4. Rectangle Class
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# 5. Car Class
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"\nCar: {self.year} {self.make} {self.model}")


# 6. Customer Class (uses JSON file)
class Customer:
    def __init__(self, name, email, balance):
        self.name = name
        self.email = email
        self.balance = float(balance)

    def display_info(self):
        print(f"Customer: {self.name}, Email: {self.email}, Balance: ${self.balance:.2f}")


def load_customers_from_json(filename="customers.json"):
    if not os.path.exists(filename):
        print(f"File '{filename}' not found. Please create it first.")
        return
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)
        for c in data:
            customer = Customer(c["name"], c["email"], c["balance"])
            customer.display_info()


# 7. Person Class
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display_info(self):
        print(f"Person: {self.name}, Age: {self.age}, Address: {self.address}")


# 8. Circle Class
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius


# 9. Product Class (uses CSV file)
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    def total_value(self):
        return self.price * self.quantity

    def display_info(self):
        print(f"{self.name} - ${self.price:.2f} x {self.quantity} = ${self.total_value():.2f}")


def load_products_from_csv(filename="products.csv"):
    if not os.path.exists(filename):
        print(f"File '{filename}' not found. Please create it first.")
        return
    with open(filename, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            p = Product(row["name"], row["price"], row["quantity"])
            p.display_info()


# 10. Movie Class
class Movie:
    def __init__(self, title, director, rating):
        self.title = title
        self.director = director
        self.rating = rating

    def display_info(self):
        print(f"Movie: '{self.title}' directed by {self.director}, Rating: {self.rating}/10")


# Menu Function
def main_menu():
    while True:
        print("\n==============================")
        print(" Object-Oriented Programming Menu ")
        print("==============================")
        print("1. Create Student")
        print("2. Load Employees from CSV")
        print("3. Bank Account Simulation")
        print("4. Rectangle Calculator")
        print("5. Create Car")
        print("6. Load Customers from JSON")
        print("7. Create Person")
        print("8. Circle Calculator")
        print("9. Load Products from CSV")
        print("10. Create Movie")
        print("0. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            s = Student("Alice", 20, [88, 92, 95])
            s.display_info()

        elif choice == "2":
            load_employees_from_csv()

        elif choice == "3":
            acc = BankAccount("Alex", 500)
            acc.deposit(200)
            acc.withdraw(100)

        elif choice == "4":
            width = float(input("Enter width: "))
            height = float(input("Enter height: "))
            r = Rectangle(width, height)
            print(f"Area: {r.area():.2f}, Perimeter: {r.perimeter():.2f}")

        elif choice == "5":
            car = Car("Toyota", "Corolla", 2022)
            car.display_info()

        elif choice == "6":
            load_customers_from_json()

        elif choice == "7":
            p = Person("John", 35, "123 Maple Street")
            p.display_info()

        elif choice == "8":
            radius = float(input("Enter radius: "))
            c = Circle(radius)
            print(f"Area: {c.area():.2f}, Circumference: {c.circumference():.2f}")

        elif choice == "9":
            load_products_from_csv()

        elif choice == "10":
            m = Movie("Inception", "Christopher Nolan", 9)
            m.display_info()

        elif choice == "0":
            print("Exiting program. Goodbye.")
            break

        else:
            print("Invalid choice, please try again.")


# Run Program
if __name__ == "__main__":
    main_menu()
