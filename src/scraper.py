from selenium import webdriver 
from selenium.webdriver.common.by import By
import time 
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

base_url = "https://aqarmap.com.eg/ar/for-sale/apartment/?page="


properties = []

MAX_PAGES = 11
for page in range(1, MAX_PAGES + 1):

    print("Opening page:", page)

    driver.get(base_url + str(page))

    WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.TAG_NAME, "article"))
    )

    cards = driver.find_elements(By.TAG_NAME,"article")

    print("Cards found:", len(cards))

    for card in cards :
        
        title = card.find_element(By.TAG_NAME, "h2").text
        price = card.find_element(By.TAG_NAME, "data").get_attribute("value")
        links = card.find_elements(By.TAG_NAME, "a")

        location = links[-2].text

        details = card.find_elements(By.TAG_NAME,"span")


        area = ""
        bedrooms = ""
        bathrooms = ""

        for detail in details :
            text = detail.text

            if "م²" in text:
                area = text

            elif text.isdigit():
                if bedrooms == "":
                    bedrooms = text
                else:
                    bathrooms = text

        properties.append({
            "title": title,
            "price": price,
            "location": location,
            "area": area,
            "bedrooms": bedrooms,
            "bathrooms": bathrooms
        })


df = pd.DataFrame(properties)

df.to_excel(r"data/real_estate.xlsx", index=False)

driver.quit()

print(f"Scraped {len(df)} properties.")
print("Data saved successfully TO data/real_estate.xlsx.")
