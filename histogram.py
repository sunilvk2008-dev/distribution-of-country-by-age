import pandas as pd
import matplotlib.pyplot as plt

# Read the Excel file
file_path = "Data_Extract_FromWorld Development Indicators.xlsx"

try:
    df = pd.read_excel(file_path)

    # Display first 5 rows
    print("First 5 rows of the dataset:")
    print(df.head())

    # Display column names
    print("\nColumns in the dataset:")
    print(df.columns)

    # Select the year to plot
    year = "2025"

    # Check if the column exists
    if year in df.columns:

        # Remove missing values
        data = df[year].dropna()

        # Create histogram
        plt.figure(figsize=(10,6))
        plt.hist(data, bins=10, edgecolor="black")

        # Add labels
        plt.title(f"Histogram of {year} Values")
        plt.xlabel(year)
        plt.ylabel("Frequency")

        # Add grid
        plt.grid(True)

        # Save the figure
        plt.savefig("histogram_2025.png")

        # Display the histogram
        plt.show()

        print("\nHistogram created successfully!")
        print("Image saved as histogram_2025.png")

    else:
        print(f"\nColumn '{year}' not found in the dataset.")

except FileNotFoundError:
    print("Excel file not found. Make sure it is in the same folder as this program.")

except Exception as e:
    print("Error:", e)