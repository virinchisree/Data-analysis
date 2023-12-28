import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import requests
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

proxy = '185.199.229.156:7492'
proxy_username = 'virinchisree'
proxy_password = 'godslayer98'
port = 7492

# Format the proxy URL with authentication
proxy_url = f"{proxy_username}:{proxy_password}@{proxy}"

# Set up the Chrome options and driver
chrome_options = Options()
chrome_options.add_argument(f'--proxy-server=http://{proxy_url}')
chrome_options.add_experimental_option('detach', True)

try:
    # Specify the path to your Chrome binary if needed
    # chrome_options.binary_location = r'Z:\Rgit(P)\chrome-win64\chrome.exe'
    
    # Use ChromeDriverManager to automatically download and manage the driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    url = "https://www.yelp.com/search?find_desc=&find_loc=San+Francisco%2C+CA&start=0"
    driver.get(url)
    driver.maximize_window()
    
    # Optional: Add a delay to observe the opened browser
    time.sleep(5)
    
except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    # Close the browser window
    if 'driver' in locals():
        driver.quit()
