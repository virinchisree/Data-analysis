import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import openpyxl
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException, NoSuchFrameException
from selenium.common.exceptions import NoSuchFrameException

#path = r'C:\Users\virin\OneDrive\Desktop\practice\Inventorysrc.xlsx'

url = "https://www.justdial.com/Visakhapatnam/Caterers-For-Parties/nct-10083387"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("user-agent=*")
chrome_options.binary_location = r'Z:\Rgit(P)\chrome-win64\chrome.exe'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
driver.get(url)
driver.maximize_window()
time.sleep(10)
#------------------------------------------------------------------------------------------------------------------------------------------------
try:
    #driver.switch_to.frame(1)
    may_be_later = driver.find_element(By.XPATH,'//span[@aria-label="May be later"]')
    may_be_later.click()
except Exception as e:
    print(f"There has been an error: {e}")
time.sleep(3)
#-------------------------------------------------------------------------------------------------------------------------------------------------
#wait = WebDriverWait(driver, 10)
#driver.execute_script("window.scrollBy(0, 8500);")
#catalog = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class = "jsx-3349e7cd87e12d75 resultbox_title_anchor  line_clamp_1"]')))
catalog = len(driver.find_elements(By.XPATH,'//div[@role = "listitem"]'))
print(catalog)

from selenium.common.exceptions import NoSuchElementException

for i in range(1, catalog + 1):
    try:
        catalog_titles = driver.find_element(By.XPATH, f'//div[{i}]/div[@role="listitem"]')
        catalog_titles.click()
        time.sleep(1)
        driver.refresh()
        time.sleep(3)
        
        caterers = driver.find_element(By.XPATH, '//h1[@class="jsx-ce80c57bc5c5e593 compney font25 fw700 color111"]').text
        print(caterers)
        
        driver.back()
        time.sleep(3)
        
    except NoSuchElementException:
        print(f"Element for iteration {i} not found. Skipping to the next iteration.")
        continue
