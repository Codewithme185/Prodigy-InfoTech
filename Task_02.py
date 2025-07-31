import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("train.csv")

# Step 1: Basic Information
print("First 5 rows:")
print(df.head())
print("\nData Summary:")
print(df.info())

# Step 2: Data Cleaning
print("\nMissing values before cleaning:")
print(df.isnull().sum())

df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
df.drop(columns=['Cabin'], inplace=True)
df.drop_duplicates(inplace=True)

print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Step 3: Exploratory Data Analysis (EDA)

# Survival Count
sns.countplot(x='Survived', data=df)
plt.title("Survival Count")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Passenger Count")
plt.show()

# Survival by Gender
sns.countplot(x='Sex', hue='Survived', data=df)
plt.title("Survival by Gender")
plt.ylabel("Passenger Count")
plt.show()

# Survival by Passenger Class
sns.countplot(x='Pclass', hue='Survived', data=df)
plt.title("Survival by Passenger Class")
plt.show()

# Age Distribution
sns.histplot(df['Age'], bins=20, kde=True)
plt.title("Age Distribution of Passengers")
plt.show()

# Age vs Survival
sns.boxplot(x='Survived', y='Age', data=df)
plt.title("Age vs Survival")
plt.show()
