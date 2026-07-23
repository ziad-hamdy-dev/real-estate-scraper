import pandas as pd

df = pd.read_excel(r"data/real_estate.xlsx")


print("Before Cleaning:")
print(df.isnull().sum())


# Remove rows without title
df = df.dropna(subset=["title"])


# Fill missing bathrooms with 0
df["bathrooms"] = df["bathrooms"].fillna(0)


# Convert price to numeric
df["price"] = pd.to_numeric(df["price"], errors="coerce")


# Remove duplicate rows
df = df.drop_duplicates()


print("\nAfter Cleaning:")
print(df.isnull().sum())


print(f"\nTotal Properties After Cleaning: {len(df)}")


# Save cleaned data
df.to_excel(r"data/cleaned_real_estate.xlsx", index=False)


print("\nCleaned data saved successfully.")