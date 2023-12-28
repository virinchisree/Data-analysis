import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Set up the Chrome options and driver
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.binary_location = r'Z:\Rgit(P)\chrome-win64\chrome.exe'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

url = "https://www.yelp.com/search?find_desc=&find_loc=San+Francisco%2C+CA&start=0"
driver.get(url)
driver.maximize_window()
time.sleep(2)
#------------------------------------------------------------------------------------------------------------
last_page = 24
for p in range(1, last_page+1):
  if p==1:
    page_title = driver.find_element(By.XPATH,'//div[@class = "pagination-link--current__09f24__vBjKh css-1jq1ouh"]').text
    print(page_title)
  else:
    next_page = driver.find_element(By.XPATH,'//a[@aria-label="Next"]').click()
    time.sleep(5)
    page_title = driver.find_element(By.XPATH,'//div[@class = "pagination-link--current__09f24__vBjKh css-1jq1ouh"]').text
    print(page_title)
