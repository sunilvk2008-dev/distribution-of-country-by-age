import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
file_path = "Data_Extract_FromWorld Development Indicators.xlsx"

try:
    # Read Excel
    df = pd.read_excel(file_path)

    # Select the year column
    year = "2025"

    # Check if the column exists
    if year not in df.columns:
        print(f"Column '{year}' not found.")
        print("\nAvailable columns:")
        print(df.columns)
        exit()

    # Convert to numeric
    data = pd.to_numeric(df[year], errors="coerce").dropna()

    # Statistics
    mean_value = data.mean()
    median_value = data.median()
    minimum = data.min()
    maximum = data.max()

    print("\nDataset Statistics")
    print("--------------------------")
    print(f"Mean   : {mean_value:.2f}")
    print(f"Median : {median_value:.2f}")
    print(f"Minimum: {minimum:.2f}")
    print(f"Maximum: {maximum:.2f}")

    # Create Figure
    plt.figure(figsize=(12,7))

    # Histogram
    plt.hist(
        data,
        bins=12,
        color="cornflowerblue",
        edgecolor="black",
        alpha=0.8
    )

    # Mean line
    plt.axvline(
        mean_value,
        color="red",
        linestyle="--",
        linewidth=2,
        label=f"Mean = {mean_value:.2f}"
    )

    # Median line
    plt.axvline(
        median_value,
        color="green",
        linestyle="--",
        linewidth=2,
        label=f"Median = {median_value:.2f}"
    )

    # Labels
    plt.title("Distribution of Population Values (2025)", fontsize=18, fontweight="bold")
    plt.xlabel("Population Value", fontsize=14)
    plt.ylabel("Frequency (Number of Countries)", fontsize=14)

    # Grid
    plt.grid(axis="y", linestyle="--", alpha=0.5)

    # Legend
    plt.legend()

    # Save image
    plt.savefig("population_histogram.png", dpi=300)

    # Display
    plt.show()

    print("\nHistogram created successfully!")
    print("Image saved as population_histogram.png")

except FileNotFoundError:
    print("Excel file not found.")

except Exception as e:
    print("Error:", e)