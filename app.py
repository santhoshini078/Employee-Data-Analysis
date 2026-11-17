
import pandas as pd
import matplotlib.pyplot as plt

# 1. Load Dataset
df = pd.read_csv("Employee.csv")

print("----- ORIGINAL DATASET -----")
print(df.head())

print("\nDataset Shape:", df.shape)

# 2. Clean the Data
print("\n----- DATA CLEANING -----")

print("Duplicate Rows:", df.duplicated().sum())

df = df.drop_duplicates()

# Check Missing Values
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# Fill Missing Values
for col in df.columns:
    if pd.api.types.is_numeric_dtype(df[col]):
        df[col] = df[col].fillna(df[col].median())
    else:
        if not df[col].mode().empty:
            df[col] = df[col].fillna(df[col].mode()[0])
        else:
            df[col] = df[col].fillna("Unknown")

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# 3. Find Averages and Maximum Values
print("\n----- AVERAGE VALUES -----")
print(df.select_dtypes(include="number").mean())

print("\n----- MAXIMUM VALUES -----")
print(df.select_dtypes(include="number").max())

# 4. Identify Missing Information
print("\n----- MISSING INFORMATION -----")
print("Total Missing Values:", df.isnull().sum().sum())

# 5. Generate Graphs

# Graph 1: Employee Age Distribution
plt.figure(figsize=(7, 5))
plt.hist(df["Age"], bins=10, edgecolor="black")
plt.title("Employee Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Employees")
plt.savefig("age_distribution.png")
plt.show()

# Graph 2: Employees in Each City
plt.figure(figsize=(7, 5))
df["City"].value_counts().plot(kind="bar")
plt.title("Employees by City")
plt.xlabel("City")
plt.ylabel("Number of Employees")
plt.savefig("city_distribution.png")
plt.show()

# Graph 3: Employee Leaving Analysis
plt.figure(figsize=(7, 5))
df["LeaveOrNot"].value_counts().plot(kind="bar")
plt.title("Employee Leaving Analysis")
plt.xlabel("Leave Or Not (0 = No, 1 = Yes)")
plt.ylabel("Number of Employees")
plt.savefig("employee_leaving.png")
plt.show()

# Save Cleaned Dataset
df.to_csv("cleaned_employee.csv", index=False)

# 6. Summary of Findings
print("\n----- SUMMARY OF FINDINGS -----")

print("Total Employees:", len(df))

print("Total Columns:", len(df.columns))

print("Average Age:", round(df["Age"].mean(), 2))

print("Maximum Age:", df["Age"].max())

print("Average Experience:",
      round(df["ExperienceInCurrentDomain"].mean(), 2))

# Newly Added
print("Maximum Experience:",
      df["ExperienceInCurrentDomain"].max())

print("Most Common City:", df["City"].mode()[0])

print("Employees Who Left:",
      (df["LeaveOrNot"] == 1).sum())

print("Employees Who Stayed:",
      (df["LeaveOrNot"] == 0).sum())

print("\nPractical Implementation Completed!")
