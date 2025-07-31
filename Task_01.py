import pandas as pd
import matplotlib.pyplot as plt

# Load dataset (skip metadata rows)
df = pd.read_csv("API_SP.POP.TOTL_DS2_en_csv_v2_38144.csv", skiprows=4)

# Drop the last unwanted column
df.drop(columns=["Unnamed: 69"], inplace=True)

# Filter only total population rows
df = df[df["Indicator Code"] == "SP.POP.TOTL"]

# Select relevant columns
df = df[["Country Name", "2022"]]

# Drop rows with missing population data
df = df.dropna(subset=["2022"])

# Convert population to float
df["2022"] = df["2022"].astype(float)

# Get top 10 most populated countries
top_10 = df.sort_values(by="2022", ascending=False).head(10)

# Print top 10
print("Top 10 countries by population in 2022:\n")
print(top_10)

# Plot bar chart
plt.figure(figsize=(10, 6))
plt.bar(top_10["Country Name"], top_10["2022"], color='skyblue')
plt.title("Top 10 Most Populated Countries (2022)")
plt.xlabel("Country")
plt.ylabel("Population")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
