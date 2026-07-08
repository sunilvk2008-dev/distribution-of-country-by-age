import pandas as pd
import matplotlib.pyplot as plt

# Read the Excel file
df = pd.read_excel("Data_Extract_FromWorld Development Indicators.xlsx")

# Rename the first column to Country
df.rename(columns={df.columns[0]: "Country"}, inplace=True)

# Convert the 2023 column to numeric
df["2023"] = pd.to_numeric(df["2023"], errors="coerce")

# Remove missing values
male_percentage = df["2023"].dropna()

# Create histogram
plt.figure(figsize=(10,6))
plt.hist(male_percentage, bins=10, edgecolor="black", color="skyblue")

plt.title("Distribution of Male Population Percentage (2023)")
plt.xlabel("Male Population (%)")
plt.ylabel("Number of Countries")

plt.grid(axis="y", linestyle="--", alpha=0.7)

plt.show()