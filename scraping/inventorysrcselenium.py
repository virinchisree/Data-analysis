import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import openpyxl
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

path = r'C:\Users\virin\OneDrive\Desktop\practice\Inventorysrc.xlsx'

url = "https://app.inventorysource.com/#/suppliers/?sort_on=popularity&sort_descending=true&supplier_type_integrated=1"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.binary_location = r'Z:\Rgit(P)\chrome-win64\chrome.exe'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
driver.get(url)
driver.maximize_window()
time.sleep(10)
#-----------------------------------------------------------------------------------------------------
username = driver.find_element(By.NAME,'email')
password = driver.find_element(By.NAME,'password')
login = driver.find_element(By.XPATH, '//*[@type = "submit"]')

username.send_keys("99.pranav@gmail.com")
password.send_keys("Pranav@1991")
login.click()
time.sleep(10)
#-----------------------------------------------------------------------------------------------------
nof_product = len(driver.find_elements(By.XPATH,'//div[@class = "supplier ng-scope"]'))
print(nof_product)
for p in range(1, nof_product+1):
    time.sleep(5)
    product_path = driver.find_element(By.XPATH,'//div[@class = "supplier ng-scope"]['+str(p)+']//h2/a').click() 
    time.sleep(5)
    title = driver.find_element(By.XPATH,'//div[@class = "flex-con title-con xs-pad-lr"]//h2').text
    print(title)
    driver.back()
