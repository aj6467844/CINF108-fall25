def concatenate_lists(list1, list2):
    return list1 + list2

def find_min_max(lst):
    return min(lst), max(lst)

def square_list(lst):
    return [x**2 for x in lst]

def common_elements(list1, list2):
    return [x for x in list1 if x in list2]

def max_length_words(words):
    max_len = max(len(word) for word in words)
    max_words = [word for word in words if len(word) == max_len]
    return max_words, max_len

def count_occurrences(lst):
    from collections import Counter
    return dict(Counter(lst))

def unique_names(names):
    return list(set(names))

def sort_by_length(strings):
    return sorted(strings, key=len)

def is_sorted(lst):
    return lst == sorted(lst)

def union_lists(list1, list2):
    return list(set(list1) | set(list2))

def main():
    while True:
        print("\nMenu:")
        print("1. Concatenate two lists")
        print("2. Find largest and smallest elements in a list")
        print("3. Square each element in a list")
        print("4. Find common elements between two lists")
        print("5. Find words with maximum length in a list")
        print("6. Count occurrences of each element in a list")
        print("7. Remove duplicate names from a list")
        print("8. Sort list of strings by length")
        print("9. Check if a list is sorted in ascending order")
        print("10. Find union of two lists")
        print("11. Exit")
        choice = input("Enter your choice (1-11): ")

        if choice == "1":
            l1 = input("Enter first list (space separated): ").split()
            l2 = input("Enter second list (space separated): ").split()
            print("Concatenated list:", concatenate_lists(l1, l2))
        elif choice == "2":
            lst = list(map(int, input("Enter numbers separated by space: ").split()))
            mn, mx = find_min_max(lst)
            print(f"Smallest: {mn}, Largest: {mx}")
        elif choice == "3":
            lst = list(map(int, input("Enter numbers separated by space: ").split()))
            print("Squared list:", square_list(lst))
        elif choice == "4":
            l1 = input("Enter first list (space separated): ").split()
            l2 = input("Enter second list (space separated): ").split()
            print("Common elements:", common_elements(l1, l2))
        elif choice == "5":
            words = input("Enter words separated by space: ").split()
            max_words, max_len = max_length_words(words)
            print(f"Words with max length ({max_len}): {max_words}")
        elif choice == "6":
            lst = input("Enter elements separated by space: ").split()
            print("Occurrences:", count_occurrences(lst))
        elif choice == "7":
            names = input("Enter names separated by space: ").split()
            print("Unique names:", unique_names(names))
        elif choice == "8":
            strings = input("Enter strings separated by space: ").split()
            print("Sorted by length:", sort_by_length(strings))
        elif choice == "9":
            lst = list(map(int, input("Enter numbers separated by space: ").split()))
            print("Sorted in ascending order" if is_sorted(lst) else "Not sorted")
        elif choice == "10":
            l1 = input("Enter first list (space separated): ").split()
            l2 = input("Enter second list (space separated): ").split()
            print("Union:", union_lists(l1, l2))
        elif choice == "11":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()