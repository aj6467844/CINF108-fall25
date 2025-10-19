import csv
import json
import matplotlib.pyplot as plt

# 1. Copy contents of one text file to another
def copy_text_file():
    src = input("Enter source text file name: ")
    dest = input("Enter destination text file name: ")
    try:
        with open(src, "r") as fsrc, open(dest, "w") as fdest:
            fdest.write(fsrc.read())
        print("File copied successfully.")
    except Exception as e:
        print("Error:", e)


# 2. Find the student with the highest score in a CSV file
def highest_score_in_csv():
    filename = input("Enter CSV file name of students: ")
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            top_student = max(reader, key=lambda x: float(x['score']))
            print(f"Highest Score: {top_student['name']} ({top_student['score']})")
    except Exception as e:
        print("Error:", e)


# 3. Count words and lines in a text file
def count_words_and_lines():
    filename = input("Enter text file name to count the words and lines: ")
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
            word_count = sum(len(line.split()) for line in lines)
        print(f"Lines: {len(lines)}, Words: {word_count}")
    except Exception as e:
        print("Error:", e)


# 4. Write list of sentences to a new text file
def write_sentences_to_file():
    sentences = [
        "Python is a versatile language.",
        "File handling is an important skill.",
        "Data analysis is powerful with Python.",
        "Matplotlib is great for visualization."
    ]
    filename = input("Enter file name to write sentences to: ")
    try:
        with open(filename, "w") as f:
            for sentence in sentences:
                f.write(sentence + "\n")
        print(f"Sentences written to {filename}")
    except Exception as e:
        print("Error:", e)


# 5. Calculate average salary of all employees in a CSV file
def average_salary_csv():
    filename = input("Enter CSV file name of employees: ")
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            salaries = [float(row['salary']) for row in reader]
        avg = sum(salaries) / len(salaries)
        print(f"Average Salary: ${avg:,.2f}")
    except Exception as e:
        print("Error:", e)


# 6. Find total sales revenue for a product in a CSV file
def total_sales_revenue():
    filename = input("Enter CSV file name of sales: ")
    product_name = input("Enter product name: ")
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            total = sum(float(row['revenue']) for row in reader if row['product'] == product_name)
        print(f"Total Revenue for {product_name}: ${total:,.2f}")
    except Exception as e:
        print("Error:", e)


# 7. Find sum of all numbers in a given text file
def sum_numbers_in_file():
    filename = input("Enter text file name for the sum: ")
    try:
        with open(filename, "r") as f:
            numbers = [float(x) for x in f.read().split() if x.replace('.', '', 1).isdigit()]
        print(f"Sum of numbers: {sum(numbers)}")
    except Exception as e:
        print("Error:", e)


# 8. Create a bar chart from a CSV file using matplotlib
def create_bar_chart():
    filename = input("Enter CSV file name for bar chart: ")
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            data = list(reader)
            x_field, y_field = data[0].keys()
            x = [row[x_field] for row in data]
            y = [float(row[y_field]) for row in data]
        plt.bar(x, y, color="skyblue")
        plt.xlabel(x_field)
        plt.ylabel(y_field)
        plt.title("Bar Chart from CSV Data")
        plt.show()
    except Exception as e:
        print("Error:", e)


# 9. Read a JSON file and extract specific information
def read_json_extract_info():
    filename = input("Enter JSON file name: ")
    try:
        with open(filename, "r") as f:
            data = json.load(f)
        print("JSON Content:")
        for key, value in data.items():
            print(f"{key}: {value}")
    except Exception as e:
        print("Error:", e)


# 10. Find average temperature for each day of the week in a CSV file
def avg_temperature_by_day():
    filename = input("Enter temperature CSV file name: ")
    try:
        temps = {}
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                day = row['day']
                temp = float(row['temperature'])
                temps.setdefault(day, []).append(temp)
        averages = {day: sum(vals)/len(vals) for day, vals in temps.items()}
        print("Average Temperature by Day:")
        for day, avg in averages.items():
            print(f"{day}: {avg:.2f}°C")
    except Exception as e:
        print("Error:", e)


# ---------------- MAIN MENU ----------------
def main():
    while True:
        print("\n" + "="*50)
        print("FILE AND DATA PROCESSING MENU")
        print("="*50)
        print("1. Copy contents of one text file into another")
        print("2. Find student with highest score in CSV file")
        print("3. Count words and lines in a text file")
        print("4. Write list of sentences to new text file")
        print("5. Calculate average salary of employees in CSV")
        print("6. Find total sales revenue for a product in CSV")
        print("7. Find sum of all numbers in text file")
        print("8. Create bar chart from CSV data")
        print("9. Read JSON file and extract info")
        print("10. Find average temperature by weekday (CSV)")
        print("0. Exit")
        print("="*50)

        choice = input("Enter your choice (0-10): ")

        if choice == "1":
            copy_text_file()
        elif choice == "2":
            highest_score_in_csv()
        elif choice == "3":
            count_words_and_lines()
        elif choice == "4":
            write_sentences_to_file()
        elif choice == "5":
            average_salary_csv()
        elif choice == "6":
            total_sales_revenue()
        elif choice == "7":
            sum_numbers_in_file()
        elif choice == "8":
            create_bar_chart()
        elif choice == "9":
            read_json_extract_info()
        elif choice == "10":
            avg_temperature_by_day()
        elif choice == "0":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


# Run the program
if __name__ == "__main__":
    main()
