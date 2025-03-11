from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import re

#initializing webdriver - this is needed because it's like human simulation when browsing the page
driver = webdriver.Chrome()

#declare connection from the page url
base_url = "https://www.tokopedia.com/hotwheelsidn/product"
driver.get(base_url)

#declare function to load all the products and price within the url page
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'prd_link-product-name')))

#declare lists for storing data
product_names = []
product_prices = []

#set max pages to scrape - use this for sample testing
max_pages = 5
current_page = 1

#declare function to scrape data from current page
def scrape_current_page():
    #scroll down to load all products
    for _ in range(10):  
        driver.execute_script("window.scrollBy(0, 1000);")  
        time.sleep(2)

    #find product and price elements
    product_elements = driver.find_elements(By.CLASS_NAME, 'prd_link-product-name')
    price_elements = driver.find_elements(By.CLASS_NAME, 'prd_link-product-price')

    for name_el, price_el in zip(product_elements, price_elements):
        name = name_el.text.strip()
        price = price_el.text.strip()
        price = re.sub(r"[^\d]", "", price)  #ensure numeric characters only

        product_names.append(name)
        product_prices.append(price)

#scrape the first page function
scrape_current_page()

# Loop through pages until no "Next" button is found or max_pages is reached
while current_page < max_pages:
    try:
        time.sleep(3)  # Small delay to ensure page loads

        # Try to find the "Next" button using its `data-testid`
        next_button = driver.find_element(By.XPATH, "//a[@data-testid='btnShopProductPageNext']")

        # Get the URL from the "href" attribute
        next_page_url = next_button.get_attribute("href")

        # If there's no href, stop the loop
        if not next_page_url:
            print("No more pages found. Stopping pagination.")
            break  

        print(f"Navigating to page {current_page + 1}: {next_page_url}")

        # Navigate to the next page
        driver.get(next_page_url)
        time.sleep(5)  # Wait for the next page to load

        # Wait until products load on the new page
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'prd_link-product-name')))

        # Scrape data from the new page
        scrape_current_page()

        # Increase the page counter
        current_page += 1

    except Exception as e:
        print(f"Pagination stopped due to error: {e}")
        break

# Close the WebDriver
driver.quit()

# Save data to a DataFrame
df = pd.DataFrame({
    'product_name': product_names,
    'product_price_rp': product_prices
})

# Export to CSV
df.to_csv(r"C:\Users\user\OneDrive\RFA _Personal Files\02. COURSE\Purwadhika_Data Engineering\Purwadhika_VS\webscraping_tokopedia\csv_output\hotwheels_5pages.csv", index=False)

print("Scraping completed and saved to CSV.")
