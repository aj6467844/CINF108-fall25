# -------------- Function Definitions --------------

# 1. Merge two given dictionaries into one
def merge_dicts():
    dict1 = {"a": 1, "b": 2}
    dict2 = {"c": 3, "d": 4}
    merged = {**dict1, **dict2}
    print("Merged Dictionary:", merged)

# 2. Find the most frequent element in a list
def most_frequent_element():
    lst = [1, 2, 3, 2, 4, 2, 5, 3]
    freq = max(set(lst), key=lst.count)
    print("Most frequent element:", freq)

# 3. Remove a key-value pair from a dictionary
def remove_key():
    sample_dict = {"name": "Alice", "age": 25, "city": "New York"}
    key_to_remove = "age"
    if key_to_remove in sample_dict:
        del sample_dict[key_to_remove]
    print("After removal:", sample_dict)

# 4. Check if two sets have any elements in common
def sets_have_common():
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    common = not set1.isdisjoint(set2)
    print("Do sets have elements in common?", common)

# 5. Find the dictionary in a list with the highest value for a specific key
def dict_with_highest_value():
    dict_list = [
        {"name": "Alice", "score": 85},
        {"name": "Bob", "score": 90},
        {"name": "Charlie", "score": 88}
    ]
    key = "score"
    highest = max(dict_list, key=lambda x: x[key])
    print("Dictionary with highest value:", highest)

# 6. Count the number of occurrences of each character in a string
def count_characters():
    text = "hello world"
    char_count = {}
    for ch in text:
        char_count[ch] = char_count.get(ch, 0) + 1
    print("Character occurrences:", char_count)

# 7. Find union, intersection and difference between two sets
def set_operations():
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    print("Union:", set1 | set2)
    print("Intersection:", set1 & set2)
    print("Difference (set1 - set2):", set1 - set2)

# 8. Sort list of dictionaries based on a specified key
def sort_dicts():
    dict_list = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 22},
        {"name": "Charlie", "age": 30}
    ]
    key = "age"
    sorted_list = sorted(dict_list, key=lambda x: x[key])
    print("Sorted dictionaries:", sorted_list)

# 9. Find the average value of all elements in a list of dictionaries
def average_value():
    dict_list = [
        {"math": 80, "science": 90},
        {"math": 85, "science": 95},
        {"math": 75, "science": 85}
    ]
    all_values = [value for d in dict_list for value in d.values()]
    avg = sum(all_values) / len(all_values)
    print("Average value:", avg)

# 10. Take list of strings and return set of unique characters present in all strings
def common_characters_in_strings():
    str_list = ["apple", "grape", "pineapple"]
    common_chars = set(str_list[0])
    for s in str_list[1:]:
        common_chars &= set(s)
    print("Common characters in all strings:", common_chars)


# -------------- Menu System --------------

def menu():
    while True:
        print("\n=== Python Function Menu ===")
        print("1. Merge two given dictionaries into one")
        print("2. Find the most frequent element in a list")
        print("3. Remove a key value pair from a dictionary")
        print("4. Check if two sets have any elements in common")
        print("5. Find the dictionary with the highest value for a key")
        print("6. Count character occurrences in a string")
        print("7. Find union, intersection, and difference between sets")
        print("8. Sort list of dictionaries by key")
        print("9. Find average value in list of dictionaries")
        print("10. Find unique characters present in all strings")
        print("0. Exit")

        choice = input("Enter your choice (0-10): ")

        if choice == "1":
            merge_dicts()
        elif choice == "2":
            most_frequent_element()
        elif choice == "3":
            remove_key()
        elif choice == "4":
            sets_have_common()
        elif choice == "5":
            dict_with_highest_value()
        elif choice == "6":
            count_characters()
        elif choice == "7":
            set_operations()
        elif choice == "8":
            sort_dicts()
        elif choice == "9":
            average_value()
        elif choice == "10":
            common_characters_in_strings()
        elif choice == "0":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# -------------- Run the Program --------------
if __name__ == "__main__":
    menu()