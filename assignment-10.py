import math
import csv
import json
import os

# === 1. Shape Base Class (Inheritance Example) ===
class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side


# === 2. Employee Hierarchy (Manager, Engineer) ===
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}, Salary: ${self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_info(self):
        print(f"Manager: {self.name}, Department: {self.department}, Salary: ${self.salary}")

class Engineer(Employee):
    def __init__(self, name, salary, specialty):
        super().__init__(name, salary)
        self.specialty = specialty

    def display_info(self):
        print(f"Engineer: {self.name}, Specialty: {self.specialty}, Salary: ${self.salary}")


# === 3. Shape Hierarchy (Triangle, Rectangle) ===
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return "Cannot determine without side lengths"


# === 4. Animal Hierarchy ===
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Bird(Animal):
    def speak(self):
        return f"{self.name} says: Tweet!"

class Fish(Animal):
    def speak(self):
        return f"{self.name} says: Blub!"


# === 5. Product (JSON + Encapsulation) ===
class Product:
    def __init__(self, name, price, quantity):
        self.__name = name
        self.__price = float(price)
        self.__quantity = int(quantity)

    def display_info(self):
        print(f"Product: {self.__name}, Price: ${self.__price}, Quantity: {self.__quantity}")

    @staticmethod
    def read_from_json(filename="products.json"):
        if not os.path.exists(filename):
            print(f"File '{filename}' not found.")
            return []
        with open(filename, "r") as f:
            data = json.load(f)
            return [Product(d["name"], d["price"], d["quantity"]) for d in data]


# === 6. Vehicle Hierarchy ===
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        pass

class Car(Vehicle):
    def drive(self):
        print(f"{self.brand} car is driving.")

class Bike(Vehicle):
    def drive(self):
        print(f"{self.brand} bike is pedaling.")

class Truck(Vehicle):
    def drive(self):
        print(f"{self.brand} truck is hauling cargo.")


# === 7. User Class (Encapsulation) ===
class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password  # private

    def display_user(self):
        print(f"Username: {self.username}, Password: {'*' * len(self.__password)}")


# === 8. Electronics Hierarchy ===
class Electronics:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Phone(Electronics):
    def call(self):
        print(f"{self.brand} {self.model} is making a call.")

class Laptop(Electronics):
    def compute(self):
        print(f"{self.brand} {self.model} is running software.")


# === 9. Employee (CSV + Private Attributes) ===
class EmployeeCSV:
    def __init__(self, name, position, salary):
        self.__name = name
        self.__position = position
        self.__salary = salary

    def display_info(self):
        print(f"Name: {self.__name}, Position: {self.__position}, Salary: ${self.__salary}")

    @staticmethod
    def read_from_csv(filename="employees.csv"):
        if not os.path.exists(filename):
            print(f"File '{filename}' not found.")
            return []
        with open(filename, newline='') as f:
            reader = csv.DictReader(f)
            return [EmployeeCSV(row['name'], row['position'], row['salary']) for row in reader]


# === 10. Shape Hierarchy (Circle, Triangle, Rectangle) ===
class Shape2D:
    def area(self):
        pass

class Circle2D(Shape2D):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Triangle2D(Shape2D):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Rectangle2D(Shape2D):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# === MENU SYSTEM ===
def main_menu():
    while True:
        print("\n=== Inheritance & Encapsulation Examples ===")
        print("1. Shape Hierarchy (Circle & Square)")
        print("2. Employee Hierarchy (Manager & Engineer)")
        print("3. Shapes (Triangle, Rectangle)")
        print("4. Animal Hierarchy (Bird, Fish)")
        print("5. Product from JSON (Encapsulation)")
        print("6. Vehicle Hierarchy (Car, Bike, Truck)")
        print("7. User Class (Encapsulation)")
        print("8. Electronics Hierarchy (Phone, Laptop)")
        print("9. Employee from CSV (Private Attributes)")
        print("10. Shape Hierarchy (Circle, Triangle, Rectangle)")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            c = Circle(5)
            s = Square(4)
            print(f"Circle Area: {c.area():.2f}, Perimeter: {c.perimeter():.2f}")
            print(f"Square Area: {s.area()}, Perimeter: {s.perimeter()}")

        elif choice == "2":
            m = Manager("Alice", 90000, "HR")
            e = Engineer("Bob", 80000, "Software")
            m.display_info()
            e.display_info()

        elif choice == "3":
            r = Rectangle(5, 3)
            t = Triangle(6, 4)
            print(f"Rectangle Area: {r.area()}, Perimeter: {r.perimeter()}")
            print(f"Triangle Area: {t.area()}, Perimeter: {t.perimeter()}")

        elif choice == "4":
            b = Bird("Parrot")
            f = Fish("Goldfish")
            print(b.speak())
            print(f.speak())

        elif choice == "5":
            products = Product.read_from_json()
            if products:
                for p in products:
                    p.display_info()

        elif choice == "6":
            car = Car("Toyota")
            bike = Bike("Trek")
            truck = Truck("Volvo")
            car.drive()
            bike.drive()
            truck.drive()

        elif choice == "7":
            u = User("ethel", "secret123")
            u.display_user()

        elif choice == "8":
            phone = Phone("Apple", "iPhone 15")
            laptop = Laptop("Dell", "XPS 13")
            phone.call()
            laptop.compute()

        elif choice == "9":
            employees = EmployeeCSV.read_from_csv()
            if employees:
                for e in employees:
                    e.display_info()

        elif choice == "10":
            c = Circle2D(5)
            t = Triangle2D(4, 3)
            r = Rectangle2D(6, 2)
            print(f"Circle Area: {c.area():.2f}")
            print(f"Triangle Area: {t.area():.2f}")
            print(f"Rectangle Area: {r.area():.2f}")

        elif choice == "0":
            print("Exiting program...")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main_menu()
