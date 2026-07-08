"""
Distribution of Female Population Share by Country (2025) — pandas version
Source: World Development Indicators (World Bank) Excel export
"""

import os
import sys
import pandas as pd
import matplotlib.pyplot as plt

FILENAME = "Data_Extract_FromWorld Development Indicators.xlsx"

# ---------- 0. Locate the file reliably ----------
# Look in: same folder as this script, then common fallback locations
script_dir = os.path.dirname(os.path.abspath(__file__))
candidates = [
    os.path.join(script_dir, FILENAME),
    os.path.join(os.path.expanduser("~"), "Downloads", FILENAME),
    os.path.join(os.path.expanduser("~"), "Desktop", FILENAME),
]

SRC = next((p for p in candidates if os.path.exists(p)), None)

if SRC is None:
    print("ERROR: Could not find the Excel file. Checked these locations:")
    for p in candidates:
        print(f"  - {p}")
    print("\nFix: either move the file into one of those folders,")
    print("or edit the SRC variable below with the exact full path.")
    sys.exit(1)

print(f"Using file: {SRC}\n")

# ---------- 1. Load & clean with pandas ----------
df = pd.read_excel(SRC, header=0)
df = df.rename(columns={df.columns[0]: "Country"})
df = df.drop(columns=[c for c in df.columns if "Unnamed" in str(c)])
df = df.iloc[:-1]                      # drop footer metadata row
df["Country"] = df["Country"].str.strip()

AGGREGATES = {
    "Arab World", "Caribbean small states", "Central Europe and the Baltics",
    "Early-demographic dividend", "East Asia & Pacific",
    "East Asia & Pacific (excluding high income)",
    "East Asia & Pacific (IDA & IBRD countries)", "Euro area",
    "Europe & Central Asia", "Europe & Central Asia (excluding high income)",
    "Europe & Central Asia (IDA & IBRD countries)", "European Union",
    "Fragile and conflict affected situations",
    "Heavily indebted poor countries (HIPC)", "High income", "IBRD only",
    "IDA & IBRD total", "IDA blend", "IDA only", "IDA total",
    "Late-demographic dividend", "Latin America & Caribbean",
    "Latin America & Caribbean (excluding high income)",
    "Latin America & the Caribbean (IDA & IBRD countries)",
    "Least developed countries: UN classification", "Low & middle income",
    "Low income", "Lower middle income", "Middle East & North Africa",
    "Middle East & North Africa (excluding high income)",
    "Middle East & North Africa (IDA & IBRD countries)", "Middle income",
    "North America", "OECD members", "Other small states",
    "Pacific island small states", "Post-demographic dividend",
    "Pre-demographic dividend", "Small states", "South Asia",
    "South Asia (IDA & IBRD)", "Sub-Saharan Africa",
    "Sub-Saharan Africa (excluding high income)",
    "Sub-Saharan Africa (IDA & IBRD countries)", "Upper middle income", "World",
}

countries = df[~df["Country"].isin(AGGREGATES)].copy()
countries = countries[countries["Country"] != "Not classified"]
countries["pct"] = pd.to_numeric(countries["2025"], errors="coerce")
countries = countries.dropna(subset=["pct"])

# ---------- 2. Quick stats with pandas ----------
mean_val = countries["pct"].mean()
median_val = countries["pct"].median()
low = countries["pct"].lt(45).sum()
mid = countries["pct"].between(45, 53, inclusive="left").sum()
high = countries["pct"].ge(53).sum()

print(countries["pct"].describe())
print(f"< 45%: {low} | 45-53%: {mid} | >= 53%: {high}")

# ---------- 3. Plot using pandas' built-in .plot.hist() ----------
ax = countries["pct"].plot.hist(
    bins=range(28, 57, 1),
    figsize=(11, 6.5),
    color="#3B82F6",
    edgecolor="white",
    linewidth=0.6,
    title="Distribution of Female Population Share by Country, 2025",
)

ax.axvline(median_val, color="#1F2937", linestyle="--", linewidth=1.2)
ax.text(median_val + 0.3, ax.get_ylim()[1] * 0.92,
        f"Median\n{median_val:.1f}%", fontsize=9, fontweight="bold")

ax.set_xlabel("Female Population (% of total population)")
ax.set_ylabel("Number of Countries")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()
out_path = os.path.join(script_dir, "histogram_female.png")
plt.savefig(out_path, bbox_inches="tight", facecolor="white")
print(f"\nChart saved to: {out_path}")
plt.show()