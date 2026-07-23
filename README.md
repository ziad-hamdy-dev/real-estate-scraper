# 🏠 Real Estate Data Scraper & Analyzer

A Python project that scrapes apartment listings from Aqarmap Egypt, stores the data in an Excel file, and performs basic data analysis using Pandas.

## 🚀 Features

- Scrape apartment listings from 12 pages of Aqarmap Egypt.
- Extract:
  - Property Title
  - Price
  - Location
  - Area
  - Bedrooms
  - Bathrooms
- Save the scraped data to an Excel file.
- Analyze the dataset using Pandas.
- Display:
  - First rows of the dataset
  - Dataset information
  - Statistical summary
  - Top 10 most expensive properties
  - Top 10 locations

## 📑 Extracted Data

The scraper collects the following information for each property:

- Title
- Price
- Location
- Area
- Bedrooms
- Bathrooms

## 🛠️ Technologies Used

- Python
- Selenium
- Pandas
- OpenPyXL

## 📂 Project Structure

```text
real-estate-scraper/
│
├── data/
│   └── real_estate.xlsx
│
├── reports/
│
├── src/
│   ├── scraper.py
│   └── analysis.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation

```bash
git clone <repository-url>

cd real-estate-scraper

pip install -r requirements.txt
```

## ▶️ Usage

Run the scraper:

```bash
python src/scraper.py
```

Run the analysis:

```bash
python src/analysis.py
```

## 📊 Output

The scraper generates:

```text
data/real_estate.xlsx
```

The analysis displays:

- Dataset preview
- Dataset information
- Statistical summary
- Most expensive properties
- Most common locations

## 📄 License

This project is for learning and portfolio purposes.

## 👨‍💻 Author

Ziad Hamdy