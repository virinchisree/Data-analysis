import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests

url = 'https://httpbin.org/ip'

proxy = '38.154.227.167:5868'

username = 'virinchisree'
password = 'godslayer98'

chrome_options = Options()
chrome_options.add_argument(f'--proxy-server={proxy}')
chrome_options.add_extension(r'ggmdpepbjljkkkdaklfihhngmmgmpggp/options.html')  # Replace with the actual path
chrome_options.add_experimental_option("detach", True)
chrome_options.binary_location = r'Z:\Rgit(P)\chrome-win64\chrome.exe'
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)
driver.maximize_window()
time.sleep(2)
#------------------------------------------------------------------------------------------------------------------
