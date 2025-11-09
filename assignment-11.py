import pandas as pd
from datetime import datetime

# Load the CSV file
df = pd.read_csv("Student Data.csv")

# 1. What is the average GPA of the Students?
avg_gpa = df["GPA"].mean()

# 2. What city contributes to the highest number of students?
most_common_city = df["City of Birth"].mode()[0]
city_count = df["City of Birth"].value_counts().iloc[0]

# 3. Whose average is better? Freshman? Sophomores? Juniors? Seniors?
avg_gpa_by_year = df.groupby("Year")["GPA"].mean().sort_values(ascending=False)
best_group = avg_gpa_by_year.index[0]
best_gpa = avg_gpa_by_year.iloc[0]

# 4. What is the average age for the data set?
df["Date of Birth"] = pd.to_datetime(df["Date of Birth"], errors='coerce')
today = pd.Timestamp.today()
df["Age"] = (today - df["Date of Birth"]).dt.days / 365.25
avg_age = df["Age"].mean()

# 5. What is the average age for each cohort? (Freshman/Sophomore/Junior/Senior)
avg_age_by_year = df.groupby("Year")["Age"].mean()

# Print results
print("--- Student Data Analysis ---")
print(f"1. Average GPA of students: {avg_gpa:.2f}")
print(f"2. City with the most students: {most_common_city} ({city_count} students)")
print("\n3. Average GPA by Year:")
print(avg_gpa_by_year)
print(f"\nHighest average GPA: {best_group} ({best_gpa:.2f})")
print(f"\n4. Average age of all students: {avg_age:.1f} years")
print("\n5. Average age by Year:")
print(avg_age_by_year)
