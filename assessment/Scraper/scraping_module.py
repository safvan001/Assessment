# scraping_app/scraping_module.py
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

def scrape_properties():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service as ChromeService
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options as ChromeOptions
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import NoSuchElementException

    # Set up Chrome WebDriver with Selenium
    chrome_service = ChromeService(executable_path='C:/Users/user/Downloads/chromedriver.exe')
    chrome_options = ChromeOptions()
    chrome_options.headless = True  # Run in headless mode (no browser window)

    # Initialize the WebDriver
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)


    cities = ['Pune', 'Delhi', 'Mumbai', 'Lucknow', 'Agra', 'Ahmedabad', 'Kolkata', 'Jaipur', 'Chennai', 'Bengaluru']
    localities = ['locality1', 'locality2', 'locality3']

    for city in cities:
        for locality in localities:
            url = f'https://www.housing.com/{city}-real-estate.htm?locality={locality}'
            driver.get(url)
            time.sleep(3)

            while True:
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                property_listings = soup.find_all('div', class_='property-listing')

                for listing in property_listings:
                    property_name = listing.find('a', class_='proName').text.strip()
                    property_cost = listing.find('div', class_='price').text.strip()
                    property_type = listing.find('div', class_='unit').text.strip()
                    property_area = listing.find('div', class_='size').text.strip()
                    property_locality = locality
                    property_city = city
                    individual_property_link = listing.find('a', class_='proName')['href']

                    # Store or process the scraped data as needed (e.g., save to MongoDB)

                try:
                    next_button = driver.find_element(By.XPATH, '//a[@title="Next Page"]')
                    next_button.click()
                    time.sleep(3)
                except NoSuchElementException:
                    break

    driver.quit()
