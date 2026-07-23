import pandas as pd

df = pd.read_excel(r"data/real_estate.xlsx")


report = []

report.append("Real Estate Data Analysis Report")
report.append("=" * 40)

report.append(f"Total Properties: {len(df)}")

report.append("\nDataset Information:")
report.append(str(df.info()))

report.append("\nStatistics:")
report.append(str(df.describe()))


report.append("\nTop 10 Most Expensive Properties:")
report.append(str(df.nlargest(10, "price")))


report.append("\nTop 10 Locations:")
report.append(str(df["location"].value_counts().head(10)))


with open(r"reports/analysis_report.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(report))


print("Analysis report saved successfully.")