import pandas as pd

def read_json_and_extract():
    # Ask for JSON file name
    file = input("Enter the JSON filename : ").strip()

    try:
        # Read the JSON file into a DataFrame
        df = pd.read_json(file)
    except ValueError:
        print("Error: Could not read the JSON file. Please check the file format.")
        return
    except FileNotFoundError:
        print("Error: File not found. Please check the filename and path.")
        return

    print("\nFull DataFrame (first 5 rows):")
    print(df.head())

    # Show available columns
    print("\nAvailable columns:")
    for i, col in enumerate(df.columns, 1):
        print(f"{i}. {col}")

    # Let the user choose which columns to extract
    selected = input("\nEnter column numbers to extract (comma-separated): ").split(',')

    try:
        selected_indices = [int(x.strip()) - 1 for x in selected]
        selected_columns = [df.columns[i] for i in selected_indices]

        # Extract and display the selected columns
        extracted = df[selected_columns]
        print("\nExtracted Data:")
        print(extracted)

    except (ValueError, IndexError):
        print("\nError: Invalid input. Please enter valid column numbers.")

if __name__ == "__main__":
    read_json_and_extract()
