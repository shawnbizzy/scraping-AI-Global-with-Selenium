from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# Function to count occurrences of a word on the page
def count_word_occurrences(driver, word):
    # Get the entire text of the page
    page_text = driver.find_element(By.TAG_NAME, "body").text
    # Count occurrences of the word (case-insensitive)
    return page_text.lower().count(word.lower())

# Selenium setup
options = Options()
options.add_argument("--headless")  # Run browser in headless mode
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--window-size=1920,1080")

service = Service(executable_path="chromedriver.exe") # Update with your chromedriver path
driver = webdriver.Chrome(service=service, options=options)

try:
    # Open the website
    url = "https://www.aiglobalmedialtd.com"
    driver.get(url)
    time.sleep(2)  # Allow time for the page to load

    # Count the occurrences of "Celebrat"
    word_to_count = "diverse"
    word_count = count_word_occurrences(driver, word_to_count)

    print(f"The word '{word_to_count}' appears {word_count} times on the website.")

finally:
    # Close the browser
    driver.quit()