import pandas as pd

df = pd.read_excel(r"data/real_estate.xlsx")

print("First 5 Rows")
print(df.head())

print("\nData Information")
df.info()

print("\nStatistics")
print(df.describe())

print("\nTop 10 Most Expensive Properties")
print(df.nlargest(10, "price"))

print("\nTop 10 Locations")
print(df["location"].value_counts().head(10))

print("\nAnalysis completed successfully.")
