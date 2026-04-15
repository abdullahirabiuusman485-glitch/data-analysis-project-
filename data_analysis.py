import pandas as pd

# Create sample dataset
data = {
    "Name": ["Ali", "John", "Fatima", "Aisha", "David"],
    "Age": [22, 24, 21, 23, 25],
    "Score": [85, 90, 78, 88, 92]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Display dataset
print("Student Data:")
print(df)

# Perform analysis
average_age = df["Age"].mean()
average_score = df["Score"].mean()

print("\nAverage Age:", average_age)
print("Average Score:", average_score)

# Save to CSV file
df.to_csv("students.csv", index=False)

print("\nData saved successfully as students.csv")