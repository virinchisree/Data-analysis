import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import json

url = "https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc"
response = requests.get(url)
proxy_data = response.json()


# Set up the Chrome options and driver
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.binary_location = r'Z:\Rgit(P)\chrome-win64\chrome.exe'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

url = "https://www.yelp.com/search?find_desc=&find_loc=San+Francisco%2C+CA&start=0"
driver.get(url)
driver.maximize_window()
time.sleep(2)

# Find and click on business titles
titles = driver.find_elements(By.XPATH, '//h3/span/a')

for title in titles:
    # Click on the title
    title.click()

    # Wait for the new tab/window to open
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

    # Switch to the newly opened tab/window
    driver.switch_to.window(driver.window_handles[-1])

    # Find the business name on the details page
    name_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//h1[@class="css-1se8maq"]')))
    name = name_element.text
    print(name)

    # Close the current tab/window and switch back to the original window
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

# Quit the driver when done
driver.quit()
