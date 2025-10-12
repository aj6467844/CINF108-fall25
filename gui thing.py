import tkinter as tk
from tkinter import messagebox, simpledialog


# ---------------- Functions ----------------

def merge_dicts():
    dict1 = {"a": 1, "b": 2}
    dict2 = {"c": 3, "d": 4}
    merged = {**dict1, **dict2}
    messagebox.showinfo("Result", f"Merged Dictionary:\n{merged}")

def most_frequent_element():
    sample_list = [1, 2, 2, 3, 4, 4, 4, 5]
    freq = max(set(sample_list), key=sample_list.count)
    messagebox.showinfo("Result", f"Most frequent element: {freq}")

def remove_key():
    sample_dict = {"name": "Alice", "age": 25, "city": "New York"}
    key = simpledialog.askstring("Input", f"Enter a key to remove from {sample_dict}:")
    if key in sample_dict:
        del sample_dict[key]
        messagebox.showinfo("Result", f"Updated Dictionary:\n{sample_dict}")
    else:
        messagebox.showwarning("Warning", "Key not found in dictionary.")

def sets_have_common():
    set1 = {1, 2, 3, 4}
    set2 = {3, 5, 6}
    common = not set1.isdisjoint(set2)
    if common:
        result = f"Sets have common elements: {set1 & set2}"
    else:
        result = "Sets do not share any common elements."
    messagebox.showinfo("Result", result)

def dict_with_highest_value():
    dict_list = [
        {"name": "Alice", "score": 85},
        {"name": "Bob", "score": 92},
        {"name": "Charlie", "score": 88}
    ]
    key = "score"
    highest = max(dict_list, key=lambda x: x[key])
    messagebox.showinfo("Result", f"Highest by '{key}':\n{highest}")


# ---------------- GUI Setup ----------------

def create_window():
    window = tk.Tk()
    window.title("Python Dictionary & Set Exercises")
    window.geometry("500x450")
    window.config(bg="#e8f0fe")

    title = tk.Label(window, text="Dictionary and Set Exercises",
                     font=("Segoe UI", 16, "bold"), bg="#e8f0fe", fg="#202124")
    title.pack(pady=15)

    # Button styling helper
    def create_button(text, command):
        return tk.Button(window, text=text, command=command, font=("Segoe UI", 11),
                         bg="#1a73e8", fg="white", activebackground="#1558b0",
                         activeforeground="white", relief="flat", width=35, height=2, bd=0)

    # Create buttons for each function
    btn1 = create_button("1.  Merge two dictionaries", merge_dicts)
    btn2 = create_button("2.  Find most frequent element in a list", most_frequent_element)
    btn3 = create_button("3.  Remove a key-value pair", remove_key)
    btn4 = create_button("4.  Check if two sets share elements", sets_have_common)
    btn5 = create_button("5.  Find dictionary with highest key value", dict_with_highest_value)

    # Arrange buttons
    for btn in [btn1, btn2, btn3, btn4, btn5]:
        btn.pack(pady=6)

    exit_btn = tk.Button(window, text="❌ Exit", command=window.destroy,
                         font=("Segoe UI", 11, "bold"), bg="#ea4335", fg="white",
                         activebackground="#c5221f", relief="flat", width=15, height=2)
    exit_btn.pack(pady=15)

    window.mainloop()


# ---------------- Run the App ----------------

if __name__ == "__main__":
    create_window()
