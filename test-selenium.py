from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = 'C:\Program Files (x86)\chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
driver = webdriver.Chrome(PATH, options=options)

driver.get('https://starwars.fandom.com/wiki/Main_Page')

search = driver.find_element_by_name('query') 
search.clear()
search.send_keys("Luke Skywalker")
search.send_keys(Keys.RETURN)

try:
    first_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "unified-search__result__title"))
    )
except:
    driver.quit()

first_link.click()
time.sleep(3)

driver.back()
driver.back()
driver.back()

driver.quit()